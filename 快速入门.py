# # 需求：在控制台输出古诗边框内容，只使用一个 print 完成。
# print("""# # # # # # # # # # #
# #   白 日 依 山 尽   #
# #   黄 河 入 海 流   #
# #   欲 穷 千 里 目   #
# #   更 上 一 层 楼   #
# # # # # # # # # # # #""")

# print(100) 
# print(2.13)
# print(True)
# print("False")
# print("Hello World")
# print(None)



# # 一次性可以定义点多个变量
# basic,add= 20.7,50
# total1 = basic + add 
# total2 =total1 + add
# print("第一个月播放量为：", total1,"万次")
# print("第二个月播放量为：", total2,"万次")

# a,b,c = 100,200,300
# d = c
# c = a
# a = b
# b = d
# type(a)
# print(type(a))
# print(c,a,b)
# print(isinstance(a,int))



# # 字符串定义
# str1 = "Hello,\\World!"
# str2 = 'Python is great!'
# str3 = """
# This is a multi-line string.
# It can span multiple lines.
# """
# print(str1)
# print(str2)
# print(str3)
# print(isinstance(str1, str),isinstance(str2, str),isinstance(str3, str))



# # 字符串的拼接
# s1 = "Hello" "World"       "!"   # python会直接拼接都是字面量
# print(s1)
# s2 = "Hello" + "World" + "!"  # 使用加号进行拼接
# print(s2)

# msg1 = "Hello"
# msg2 = "World"
# print("孙文涛说:" + msg1 + "，" + msg2 )  # 使用加号拼接变量

# s3 = "涛哥"
# s4 = 18
# s5 = "软件工程"
# s6 = "python" 
# print("大家好，我是" + s3 + ",今年" + s4 + ",我的专业是" + s5 + "，我喜欢" + s6 + ".")
# print("大家好，我是" + s3 + ",今年" + str(s4) + ",我的专业是" + s5 + "，我喜欢" + s6 + ".")  # 使用加号拼接多个变量和字符串
# print("大家好，我是%s,今年 %s,我的专业是%s，我喜欢%s ." % (s3, s4, s5, s6))  # 使用格式化字符串拼接多个变量和字符串
# print(f"大家好，我是{s3},今年 {s4},我的专业是，我喜欢{s6} .")  # 使用f-string拼接多个变量和字符串

# print(f"你是{s3}吗？")  # f-string中可以直接使用变量


# 键盘的数据输入
# total = 10000
# correct_password = "wbsSWT112"

# while True:
#     password = input("请输入你的银行卡密码：")
#     if password == correct_password:
#         break
#     print("密码错误，请重新输入。")

# while True:
#     try:
#         money = float(input("请输入你想取出的金额："))
#         if money <= 0:
#             print("取款金额必须大于0，请重新输入。")
#         elif money > total:
#             print("余额不足，请重新输入取款金额。")
#         else:
#             total = total - money
#             print(f"已成功取出{money}元，剩余{total}元。")
#             break
#     except ValueError:
#         print("输入的金额无效，请输入数字。")


# 算数运算符
# print(10 + 5)  # 加法
# print(10 - 5)  # 减法
# print(10 * 5)  # 乘法
# print(10 / 5)  # 除法，结果是浮点数
# print(10 // 5) # 整除，结果是整数
# print(10 % 5)  # 取模，结果是0
# X = float(input("请输入一个数字："))
# Y = float(input("请输入另一个数字："))
# print(f"加法得到{X + Y}")

# 练习1 
# x = int(input("请输入第一个整数："))
# y = int(input("请输入第二个整数："))
# z = int(input("请输入第三个整数："))
# print(f"三个整数的平均数为{(x + y + z) / 3}")

# # 练习2
# x = float(input("梯形的上底："))
# y = float(input("梯形的下底："))
# z = float(input("梯形的高："))
# print(f"梯形的面积为{(x + y) * z / 2}")

# # 练习3
# x = float(input("请输入圆的半径："))
# print(f"圆面积为{3.14 * x  ** 2},周长为{2 * 3.14 * x}")

# # 练习4
# x = float(input("请输入体重(kg):"))
# y = float(input("请输入身高(m):"))
# print(f"您的BMI指数为{x / y ** 2}")

# 比较运算符
# x = float(input("请输入第一个数字："))
# print(f"第一个数字是偶数吗？{x % 2 ==0}")

# 逻辑运算符
# x = float(input("请输入第一个数字："))
# print(f"{x}位于10-20之间吗{x > 10 and x < 20}") 
# print(f"这个数位不在于10-20之间吗?{not (x > 10 and x < 20)}") 

# if练习1
# x = int(input("请输入你的账号："))
# y = int(input("请输入你的密码："))
# if x == 123456 and y == 123456:
#     print("登录成功！")
# else:
#     print("账号或密码错误！")

# 练习2 
# x = int(input("请输入你想验证的年份 ："))
# if (x % 100 != 0 and x % 4 == 0)  or x % 400 == 0 :
#     print(f"{x}是闰年")
# else:
#     print(f"{x}不是闰年")

# 练习3
# x = int(input("请输入一个整数："))
# if x > 0:
#     if x % 2 == 0:
#         print(f"{x}是正偶数")
#     print(f"{x}是正数")
# elif x < 0:
#     print(f"{x}是负数")
# else:
#     print(f"{x}是0")


# 练习4
# x = input("请输入你的账号：")
# y = int(input("请输入你的密码："))
# if (x == "admin" and y == 666888) :
#     print("登录成功！")
# elif x == "root" and y == 123456:
#     print("登录成功！")
# elif x == "user" and y == 888666:
#     print("登录成功！")
# else:    
#     print("账号或密码错误！")

# 练习5
# x = int(input("请输入三角形的边长："))
# y = int(input("请输入三角形的边长："))
# z = int(input("请输入三角形的边长："))
# if x == y == z:
#     print("这是一个等边三角形")
# elif x == y or x == z or y == z:
#     print("这是一个等腰三角形")
# elif x ** 2 + y ** 2 == z ** 2 or x ** 2 + z ** 2 == y ** 2 or y ** 2 + z ** 2 == x ** 2:
#     print("这是一个直角三角形")
# elif x + y > z and x + z > y and y + z > x:
#     print("这是一个普通三角形")
# else:
#     print("这三条边不能构成三角形")

# 重点逻辑练习
# x = int(input("请输入三角形的边长："))
# y = int(input("请输入三角形的边长："))
# z = int(input("请输入三角形的边长："))
# if x + y > z and x + z > y and y + z > x:
#     if x == y == z:
#         print("这是一个等边三角形")
#     elif x == y or x == z or y == z:
#         print("这是一个等腰三角形")
#     elif x ** 2 + y ** 2 == z ** 2 or x ** 2 + z ** 2 == y ** 2 or y ** 2 + z ** 2 == x ** 2:
#         print("这是一个直角三角形")
#     else:
#         print("这是一个普通三角形")
# else:
#     print("这三条边不能构成三角形")


# x = float(input("请输入你使用的点度："))
# if x < 2880:
#     print(f"你使用的点度为{x}，电费为{0.4883 * x}元")
# elif 2880 <= x < 4800:
#     print(f"你使用的点度为{x}，电费为{0.4883 * 2880 + 0.5383 * (x - 2880)}元")
# else:
#     print(f"你使用的点度为{x}，电费为{0.4883 * 2880 + 0.5383 * 1920 + 0.6883 * (x - 4800)}元")


# day = int(input("请输入你选择的星期几(1-7):"))
# match day:
#     case 1:
#         print("今天是星期一")
#     case 2:
#         print("今天是星期二")
#     case 3:
#         print("今天是星期三")
#     case 4:
#         print("今天是星期四")
#     case 5:
#         print("今天是星期五")
#     case 6:
#         print("今天是星期六")
#     case 7:
#         print("今天是星期日")
#     case _:
#         print("输入错误，请输入1-7之间的整数")



# match case练习



# x = int(input("请输入一个整数："))

# y = int(input("请输入另一个整数："))
# z = input("请输入运算符：")
# match z:
#     case "+":
#         print(f"{x}{z}{y}={x + y}")
#     case "-":
#         print(f"{x}{z}{y}={x - y}")
#     case "*":
#         print(f"{x}{z}{y}={x * y}")
#     case "/" if y != 0:
#         print(f"{x}{z}{y}={x / y}")
#     case _:
#         print("输入错误，请输入 +、-、*、/ 中的一个")




# while循环
# i = 1
# x = 0
# while i <= 100:
#     if i % 2 == 0:
#         x += i
#     i += 1
# else:
#     print(f"偶数之和为{x}")\

# x = range(1,101,2)
# y = 0
# for i in x:
#     y += i
# print(f"{y}")

# x = range(100,501)
# y = 0 
# for i in x:
#     if i % 3 == 0:
#         y += i
# else:
#     print(f"{y}")



# 嵌套循环
# x = int(input("你想打印长度为："))
# y = int(input("你想打印宽度为："))
# for j in range(y):
#     for i in range(x):
#         print("*",end="  ")
#     print()

# 打印 99乘法表
# for j in range(1,10):
#     for i in range(1,j+1):
#         print(f"{i}x{j}={j*i}",end="\t")
#     print()



# 综合练习1
# while True:
#     try:
#         x = input("请输入你的账号")
#         y= input("请输入你的密码")
#         if x == "" or y =="":
#             print("账号密码不能为空")
#             continue
#         if x == "admin" and y == "666888" or x == "zhangsan" and y == "123456" or x == "sun" and y == "888565":
#             print("登陆成功")
#             break
#         else:
#             print("用户账号或者密码输入错误")
#     except ValueError:
#         print("输入的账号密码无效，不能为空。")

# import random
# random_num = random.randint(1,100)
# while True:
#     user_num= int(input("请输入你认为的数字："))
#     if user_num == random_num:
#         print(f"猜测正确，数迷正是{user_num}")
#         break
#     elif user_num > random_num:
#         print("你猜测的数字比字谜数字大")
#         continue
#     elif user_num < random_num:
#         print("你猜测的数字比字谜数字小")
        
    



# 列表
# user=['liangdianshui','twowater','两点水']
# print(len(user))
# print(f'{user[0]},{user[1]},{user[2]}')
# user.append('sun')
# user.insert(0,"vip")
# print(user)
# user.pop()
# print(user)
# user.pop(1)
# print(user)
# user[2] = "三点水"
# print(user)



# tuple1 = ('两点水', 'twowter', 'liangdianshui', 123, 456)
# tuple2 = '两点水', 'twowter', 'liangdianshui', 123, 456
# tuple3 = ()
# tuple4 = (123,)
# tuple5 = (123)
# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(tuple4)
# print(tuple5)
# # 查询元组
# print(tuple1[1])
# print(tuple2[0])
# 修改元组
# list = [1,2,3]
# tunlp = ('kdasjd','asdja','a',list)
# list[0] = 2
# print(tunlp)

# name1 = ('一点水', '两点水', '三点水', '四点水', '五点水')
# print(len(name1))
# print(name1 * 2)




# list = []
# x =0
# while x < 10:
#     num = int(input("输入有效数字"))
#     list.append(num)
#     x += 1
# list.sort()
# print(list)
# print(max(list))
# print(min(list)) 
# for i in list:
#     x += i
# print(f"平均值为{x / len(list)}")



# list1 = [1,2,3,4,5,6]
# list2 = [5,6,7,8,9]
# list_new = list1 + list2
# list_kong = []
# for i in list_new:
#     if i not in list_kong:
#         list_kong.append(i)

# print(list_kong)


# x = 1
# list = []
# list2 = []
# while x < 21:
#     list.append(x**2)
#     x += 1
# for i in list:
#     if i % 2 ==0:
#         list2.append(i**2)

# print(list2)



# text = input("输入字符串：")
# if  text[0:] == text[::-1]:
#     print("输入字符串为回文")
# else:
#     print("输入字符串不是回文")
# print(text[0:])
# print(text[:])

# list=[]
# for i in range(0,10):
#     text = input("请输入字符串:")
#     text2 = text.upper()
#     list.append(text2)
# for x in list:
#     print(x)   

# t1 = (5,6,7,8)
# x,*y,z = t1
# print(x,y,z)  x为5，y为[6,7],z为8

# a = 100
# b = 200
# c = 300
# c,a,b = a,b,c
# print(c,a,b)
# # 计算每个学生总分、各科平均分然后输出出来
# students = (
#     ("S001", "王林", 85, 92, 78),
#     ("S002", "李慕婉", 92, 88, 95),
#     ("S003", "十三", 78, 85, 82),
#     ("S004", "曾牛", 88, 79, 91),
#     ("S005", "周轶", 95, 96, 89),
#     ("S006", "王卓", 76, 82, 77),
#     ("S007", "红蝶", 89, 91, 94),
#     ("S008", "徐立国", 75, 69, 82),
#     ("S009", "许木", 86, 89, 98),
#     ("S010", "遁天", 66, 59, 72),
# )

# for 学号, 姓名, 语文, 数学, 英语 in students:
#     total = 语文 + 数学 + 英语
#     avg = total / 3
#     print(f"{学号} {姓名} {语文} {数学} {英语} {total} {avg:.1f}")

# # 统计各科最低和最高分
# chinese_score = [i[2] for i in students]  #语法格式[要插入改列表的值 for i in 需要遍历的序列/列表]
# print(f"{min(chinese_score)}")


# dict = {'同学1': {'语文': 85, '数学': 92, '英语': 78}}
# a = dict.items()
# print(a)








# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# print("同时选秀法语和艺术的学生有：",french_set & art_set)
# print("同时选秀四门课的学生有：",football_set & basketball_set & french_set & art_set)
# print("选秀足球但是没有选秀篮球的：",football_set - basketball_set)
# all_student = football_set.union(basketball_set,french_set,art_set)
# all = [*football_set,*basketball_set,*french_set,*art_set]
# for s in all_student:
#     print(f"{s}选修了{all.count(s)}门课程")


# s='''
# ########## 购物车系统 ########
# #                           #
# # 1. 添加购物车              #
# # 2. 修改购物车              #
# # 3. 删除购物车              #
# # 4. 查询购物车              #
# # 5. 退出购物车              #
# #                           #
# #############################
# '''
# print(s)
# shop_car = {}
# while True:
#     b = input('请选择要执行的操作(1-5):')
#     match b:
#         case '1':
#             a = input('请输入要添加商品的名称：')
#             c = input('请输入要添加商品的价格：')
#             d = input('请输入要添加商品的数量：')
#             shop_car[a] = {'价格':c,'数量':d}
#             print('添加成功',shop_car)
#         case '2':
#             a = input('请输入要修改商品的名称为：')
#             if a not in shop_car.keys()
#                 print("该商品不存在")
#                 continue
#             c = input('请输入要修改商品的价格为：')
#             d = input('请输入要修改商品的数量为：')
#             shop_car[a] = {'价格':c,'数量':d}
#             print('修改完成',shop_car)
#         case '3':
#             a = input('请输入要删除商品的名称为：')
#             shop_car.pop(a)
#         case '4':
#             a = input('请输入要查询商品的名称为：')
#             print(f'商品名称为：{a},商品价格：{shop_car[a]['价格']},商品数量：{shop_car[a]['数量']}')
#         case '5':
#             print('已退出购物车')
#             print(f'{shop_car}')
#             break
#         case _:
#             print('非法操作，不支持')
    
  
# def main(r):
#     '''
#     计算圆的面积和周长
#     r: 圆的半径
#     return: 圆的面积和周长
#     '''
#     area = 3.14 * r *r 
#     zhouchang= 2 * 3.14 * r
#     return area,round(zhouchang,1)
# help(main)
# a = main(10)
# print(a)
# area,zhouchang = main(10)
# print(f"面积为{area},周长为{zhouchang}")


# def Triangle_area(s,h):
#     """
#     计算三角形面积
#     s:三角形底
#     h:三角形高
#     return:三角形面积
#     """
#     area = s * h /2
#     return area
# area = Triangle_area(10,5)
# print(f"三角形面积为{area}")
# --------------------------------------
# def count_english(a):
#     """
#     统计传入字符串中的元音字母个数
#     a:传入的字符串
#     return:元音字母个数
#     """

#     count = 0
#     for i in a:
#         if i in "aeiouAEIOU":
#             count +=1
#     return count
# count = count_english("Hello World")
# print(f"元音字母个数为{count}")
# ------------------------------------------
# dict = {'name1':{'语文': 85, '数学': 92, '英语': 78}}
# def get_student_score(a):
#     """
#     获取学生的成绩
#     a:传入的字典
#     return:学生的成绩
#     """
#     max_score = max(dict['name1'].values())
#     min_score = min(dict['name1'].values())
#     average_score = sum(dict['name1'].values()) / len(dict['name1'])
#     return round(max_score,1),round(min_score,1),round(average_score,1)
# max_score,min_score,average_score = get_student_score(dict)
# print(f"学生的成绩最高为{max_score}")
# print(f"学生的成绩最低为{min_score}")
# print(f"学生的成绩平均为{average_score}")

# def score_level(score):
#     """
#     根据成绩判断等级
#     score:传入的成绩
#     return:成绩等级
#     """
#     if score >= 90:
#         return "优秀"
#     elif score >= 80:
#         return "良好"
#     elif score >= 70:
#         return "中等"
#     elif score >= 60:
#         return "及格"
#     else:
#         return "不及格"
# score = score_level(85)
# print(f"成绩等级为{score}")


# def string(string):
#     """
#     判断一个字符串是不是回文串
#     string:传入的字符串
#     return:判断是不是回文串
#     """
#     if string[0:] == string[::-1]:
#         return True
#     else:
#         return False
# strin = string("abcba")
# print(f"字符串是不是回文串{string}")



# def time_transform(time):
#     """
#     将秒转换为小时、分钟、秒
#     time:传入的秒数
#     return:转换后的小时、分钟、秒
#     """
#     seconds = time
#     minutes = seconds // 60
#     hours = minutes // 60
#     return hours, minutes,seconds
# hours, minutes, seconds = time_transform(3661)
# print(f"转换后的时间为：{hours}小时、{minutes}分钟、{seconds}秒")



# def Triangle_judgment(a,b,c):
#     """
#     判断三角形类型
#     a:传入的第一条边
#     b:传入的第二条边
#     c:传入的第三条边
#     return:三角形类型
#     """
#     if a + b > c and a+c >b and b+c >a:
#         if a==b==c:
#             return "等边三角形"
#         elif a==b or a==c or b==c:
#             return "等腰三角形"
#         elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#             return "直角三角形"
#         elif a + b > c and a + c > b and b + c > a:
#             return "普通三角形"
#     else:
#         return "不能构成三角形"
# kind = Triangle_judgment(3, 4, 5)
# print(f"三角形类型为{kind}")

# num = 1
# def ceshi(name  ,age,name2,age2=22):
#     print(f"姓名为{name},年龄为{age},姓名为{name2},年龄为{age2}")
#     return {"name":name,"age":age,"name2":name2,"age2":age2}
# biao=ceshi(name2="张三", name="李四", age=25)
# print(biao)

def ceshi2(*arge,**kwargs):
    """
    计算任意数量数字的最大值、最小值和平均值
    arge: 传入的数字
    return: 最大值、最小值和平均值
    """
    max_num = max(arge)
    min_num = min(arge)
    avg= sum(arge) / len(arge)
    if kwargs.get("round"):
        avg = round(avg,kwargs.get("round"))
    return max_num,min_num,avg
a,b,c=ceshi2(2,43,5,75,75,43,24,90)
print(f"最大值为{a},最小值为{b},平均值为{c}")


def add(x,y):
    return x+y

def diaoyong(x,y,a):
    return a(x,y)

print(diaoyong(1,2,add))























