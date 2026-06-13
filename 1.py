# author:dayin
# Date:2019/12/17 0017
import time
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pymongo import MongoClient
import threading
from queue import Queue


# 创建一个锁对象 当一个线程进行数据库的写入时 锁上 存储信息完毕后释放
lock = threading.Lock()
# 创建一个同步条件,用于任务结束的标志
event = threading.Event()


class ZhiLianSpider(object):
    # 定义类属性 生产者 和消费者
    pname = ['生产者1号', '生产者2号', '生产者3号', '生产者4号']
    cname = ['消费者1号', '消费者2号', '消费者3号']

    def __init__(self, start, end, urlqueue, dataqueue):
        self.start = start
        self.end = end
        self.url = r'https://sou.zhaopin.com/?p={}&jl=489&kw=python&kt=3&sf=0&st=0'
        self.urlqueue = urlqueue
        self.dataqueue = dataqueue

    # run 方法执行返回完整页面的 url
    def run(self) -> None:
        for page in range(self.start, self.end + 1):
            self.urlqueue.put(self.url.format(page))

    def create_producer(self):
        '''
        为了不使 main 函数中有太多冗余 将创建生产者和消费者放在这个类方法中
        :return:
        '''
        for name in self.pname:
            p = Producer(data_queue=self.dataqueue, url_queue=self.urlqueue, name=name)
            # 启动线程
            p.start()

    def create_customer(self):
        for name in self.cname:
            c = Customer(self.dataqueue, name)
            c.start()


class Producer(threading.Thread):
    '''
    封装一下 Edge 浏览器的无头浏览器参数
    '''
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    def __init__(self, data_queue, url_queue, name):
        super(Producer, self).__init__()
        self.data_queue = data_queue
        self.url_queue = url_queue
        self.name = name

    def run(self) -> None:
        '''
        这里 run 方法主要实现两个方法 ① 下载页面 ② 将页面存到 data_queue 队列中
        :return:  这里的 ->None 表示返回的是空
        '''
        while True:
            if self.url_queue.empty():
                event.set()
                break
            url = self.url_queue.get()
            # 下载页面
            print('我是{}---->>>>正在下载页面{}'.format(self.name, url.split('?')[1].split('&')[0]))
            self.download_html(url)
            print('我是{}---->>>>已完成下载页面{}'.format(self.name, url.split('?')[1].split('&')[0]))

    def download_html(self, url):
        # 使用 Service 类指定 EdgeDriver 的路径，这里假设 edgedriver.exe 在当前目录下，根据实际情况修改路径
        service = Service('D:\\Anaconda\\msedgedriver.exe')
        # 创建一个浏览器对象
        browser = webdriver.Edge(service=service, options=self.options)
        # 打开 url
        browser.get(url)
        # 等待 1 秒
        time.sleep(1)
        # 处理弹出的按钮
        try:
            button = browser.find_element(By.CSS_SELECTOR, 'body > div.a-modal.risk-warning > div > div > button')
            # 点击按钮
            button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")
        browser.implicitly_wait(3)
        # 等待 js 内容渲染
        time.sleep(2)
        # 将页面源码存入队列中
        self.data_queue.put(browser.page_source)
        # 最后最后一定要记得关闭浏览器！ 因为这个函数是写在一个循环中的
        browser.quit()


class Customer(threading.Thread):
    # 初始化 mongodb 参数
    # 连接服务器
    conn = MongoClient(host='192.168.43.115', port=27017)
    # 创建数据库
    db = conn.zhaopin
    # 创建集合
    collection = db.zhaopin_collection

    def __init__(self, data_queue: Queue, name):
        super(Customer, self).__init__()
        self.data_queue = data_queue
        self.name = name

    def run(self) -> None:
        while True:
            # 获取页面内容进行解析
            if self.data_queue.empty() and event.is_set():
                print('任务完成...')
                break
            content = self.data_queue.get()
            print('我是{},我正在解析...'.format(self.name))
            self.parse_content(content)
            print('我是{},已经完成解析...'.format(self.name))

    def parse_content(self, content):
        '''
        观察网站源码发现 所有的招聘内容放在了一个 div 容器中 取出这个容器 循环遍历即可
        <div id="listContent" class="contentpile__content">
        :param content:
        :return:
        '''
        # 创建一个列表用于存储字典信息
        info_list = []
        soup = BeautifulSoup(content, 'lxml')
        div_lst = soup.find('div', id='listContent')
        try:
            for item in div_lst:
                try:
                    # 岗位名称
                    jobname = item.find('span', class_='contentpile__content__wrapper__item__info__box__jobname__title')['title']
                    # 工资
                    saray = item.find('p', class_='contentpile__content__wrapper__item__info__box__job__saray').text
                    # 地区
                    area = item.find_all('li', class_='contentpile__content__wrapper__item__info__box__job__demand__item')[0].text
                    # 经验
                    ex = (item.find_all('li', class_='contentpile__content__wrapper__item__info__box__job__demand__item')[1].text.strip(),
                          item.find_all('li', class_='contentpile__content__wrapper__item__info__box__job__demand__item')[2].text.strip())
                    # 公司名
                    company_name = item.find('a',
                                         class_='contentpile__content__wrapper__item__info__box__cname__title company_title').text

                    # 将信息存储为字典
                    item_info = {
                        '岗位名称': jobname,
                        '工资': saray,
                        '地区': area,
                        '经验': ex,
                        '公司名': company_name
                    }
                    info_list.append(item_info)

                except Exception:
                    continue
        except Exception as e:
            print(e)
        # 写入数据库
        lock.acquire()
        self.collection.insert_many(info_list)
        lock.release()


def main():
    startpage = eval(input('输入起始页码:'))
    endpage = eval(input('输入结束页码:'))
    # page 队列
    url_queue = Queue()
    # html 内容队列
    data_queue = Queue()
    spider = ZhiLianSpider(startpage, endpage, url_queue, data_queue)
    # 执行 run 方法返回一个 url 队列
    spider.run()
    # 创建生产者
    spider.create_producer()
    # 创建消费者
    spider.create_customer()


if __name__ == '__main__':
    main()