import requests
from urllib.parse import urlencode  # 解决编码问题
import json
import pymysql
def main(offset):
    json_page = get_page(offset,cityName,keyWord)       # 发送请求，获得json数据
    contentList = get_information(json_page)            # 提取json数据对应的字段内容

    for content in contentList:                     # 循环持久化
        write_to_file(content)
        #save_data_sql(content)
if __name__=='__main__':
    cityName = str(input('请输入查找的地区：'))
    keyWord = str(input('请输入查找的职位关键字：'))
    needPage = int(input('请输入要爬取的页数(页/90条)：'))
    # 控制爬取的页数
    for i in range(needPage):
        main(offset=90*i)   # 分析url知首页是90开始的，翻页是其倍数。

           # 在数据库新建表以后在打开这个



# 起始页，城市名，岗位词
def get_page(offset,cityName,keyWord):

    # 有反爬，添加一下header
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 73.0.3683.103Safari / 537.36'
    }

    #　构建参数组
    params = {
        'start': offset,
        'pageSize': '90',
        'cityId': cityName,
        'salary': '0,0',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        'kw': keyWord,
        'kt': '3',
        '_v': '0.12973194',
        'x-zp-page-request-id': '9bf58a63b73746ea9fd0cb8bd75560b9-1572848879239-667477',
        'x-zp-client-id': '0470c445-5e49-43bc-b918-0330e0ead9ee'
    }
    base_url = 'https://fe-api.zhaopin.com/c/i/sou?'
    url = base_url + urlencode(params) # 拼接url,要进行编码。
    print('爬取的URL为：',url)
    try:
        resp = requests.get(url,headers=headers,timeout=5)
        print(resp.text)
        if 200 == resp.status_code:  # 状态码判断
            print(resp.json())
            return resp.json()
    except requests.ConnectionError:
        print('请求出错')
        return None

def get_information(json_page):
    if json_page.get('data'):
        results = json_page.get('data').get('results')
        print(results)
        for result in results:
            yield {         #yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。
                'number':result.get('number'),                    # 编号
                'jobName': result.get('jobName'),               #岗位名称
                'city': result.get('city').get('display'),      # 城市地区
                'company': result.get('company').get('name'), # 公司名字
                # 'welfare':result.get('welfare'),              #福利信息
                'workingExp':result.get('workingExp').get('name'), # 工作经验
                'salary':result.get('salary'),                  #薪资范围
                'eduLevel':result.get('eduLevel').get('name')#学历
            }
    print('success!')

def save_data_sql(content):
    # 假设已经建立了数据库连接
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        database='job_db'
    )
    cursor = conn.cursor()
    sql = """
    INSERT INTO job_table (number, jobName, city, company, workingExp, salary, eduLevel)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            content['number'],
            content['jobName'],
            content['city'],
            content['company'],
            content['workingExp'],
            content['salary'],
            content['eduLevel']
        ))
        conn.commit()
    except pymysql.MySQLError as e:
        print(f"Error occurred while saving data to SQL: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
# 本地备份爬取的数据
def write_to_file(content):
    #print('dict:',type(content))
    with open('result.txt','a',encoding='utf-8') as f:
        #print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')  #将字典或列表转为josn格式的字符串

