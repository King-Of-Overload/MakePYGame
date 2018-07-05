#example 1.1
# pi = 3.1415926
# r = eval(input("请输入圆的半径:"))   #input输入函数，返回用户输入的数据
# s = pi*r*r
# print("半径为:",r,"圆的面积为:",s)

#求一元二次方程
# a = eval(input("请输入a:"))
# b = eval(input("请输入b:"))
# c = eval(input("请输入c:"))
# d = b ** 2 - 4* a* c; #  delta = b^2 - 4ac    **为乘方表达式
# if d >= 0:
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     print("方程的根: x1=%f,x2=%f" %(x1,x2))
# else:
#     print("input data error!")

#import 导入标准模块sys
# import sys
# print("命令行参数如下：")
# print(sys.argv)
# for i in sys.argv:
#     print(i)


#基本数据类型

#复数型 a+bj
# x = 12.3 + 45j
# print(x.real) #打印实部
# print(x.imag) #打印虚部

#字符串类型
# str = '小缘萌萌哒'
# str1 = '幼儿缘'
# str2 = '''Look 
# What You Made Me Do''' #多行字符串有三引号表示
# print(str1)
# print(str2)

# 布尔类型 1真 0假
# x = True
# int(x)
# y = False
# int(y)

#常量与变量

#变量重新赋值地址会发生变化
# x = 127
# print(id(x)) #id函数可以返回地址
# x = 255
# print(id(x))

#赋值方式
# a = 0 #一般赋值
# x += 5 #增量赋值
# a = b = c = d = 100 #链式赋值
# y, z = 3, 5 #多重赋值 左右两边个数要一致，按顺序进行赋值

# 实现两个数字交换
# a,b = 3,5
# a,b = b,a
# print(a)
# print(b)

#位运算符
# a = 0011 1100
# b = 0000 1101
# print(a&b) # 0000 1100 与运算
# print(a|b) # 0011 1101 或运算
# print(a^b) # 0011 0001 异或运算(两个不同才为1)
# print(~a) #  1100 0011 取反运算

#身份运算符 is判断是不是引用同一个对象
# x = 10
# y = 20
# x = y
# print(x is y)

#常用内置函数
# print(abs(10),abs(-10)) #取绝对值   10 10
# print(divmod(10,4),divmod(10.5,2.5)) #返回a与b的商与余数组成的元组对象 (2,2) (4,0.5)
# print(pow(2,3),pow(2,3,4)) #幂计算，两个参数计算a的b次幂，如果为三个参数，则返回x的y次幂与z的模(商的整数部分)
# print(round(3.1415926,3),round(3.1415926)) #进行四舍五入，保留几位小数

#数制转换函数
# print(int(3.14)) #3
# print(int(2e2)) # 200
# print(int('23',16)) #若有后面的参数，前面必须为字符串，后面参数为转换计数，范围[2,16] 进制
# print(int('0x10',16)) #  16

#进制转换
# b = 255
# print(bin(b), hex(b), oct(b)) #bin将十转为二  hex将十转为十六，oct将十转换为八

#类型转换
# x,y = 0,1
# print(bool(x),bool(y))#返回布尔值
# print(float(0.15)) #返回float
# x = 1
# eval('x+1') # 2 eval将字符串当成有效的表达式求值
# a = '5,10'
# x,y = eval(a)
# print(x,y)

#集合运算函数

#all函数，元素均为True或者都为空时返回True
# any函数，至少有一个True返回True，元素为空返回False
# print(all([1,2,3]),all([0,1,2]),all([])) # True False Flase
# print(any([1,2,3]),any([0,1,2]),any([])) # True True False

# range产生一个序列，第一个参数开始序列，第二个为结束序列，第三个为步长
# list从序列中生成一个列表
# tuple 产生一个元组
# help帮助函数
# x = range(1, 10, 2)
# print(list(x)) #[1,3,5,7,9]
# print(tuple(x))#(1,3,5,7,9)
# help(round)


#random 模块
# from random import *
# x = [1,2,3,4,5]
# print(sample(x,2)) #从序列x中随机挑选k个元素
# shuffle(x) #无返回值  将序列内的元素随机排序
# print(x)

#time 模块
#from time import *
# print(time()) #返回当前浮点秒数
# print(asctime()) # 返回当前系统的日期和时间的字符串
# print(strftime('%Y-%m-%d %H:%M:%S')) #时间格式化

#caledar 模块
# from calendar import *
# print(month(2017,5))#多行输出2017年 5月的日历
# print(weekday(2018,5,20)) #返回该日的星期代码，0-6代表星期
# print(monthrange(2017,5)) #2017年5月第一天是星期一，有31天

# 单分支结构  输出最大数
# x = eval(input("请输入第一个数字："))
# y = eval(input("请输入第二个数字："))
# print("输入的两个数字为：",x, y)
# if x > y:
#     print("较大的是:",x)
# if x < y:
#     print("较大的是:",y)

#多分支结构
#输出最大数
# x = eval(input("请输入第一个数字："))
# y = eval(input("请输入第二个数字："))
# print("输入的两个数字为：",x, y)
# if x > y:
#     print("较大的是：",x)
# elif x < y:
#     print("较大的是：",y)
# else:
#     print("这两个数字相等")

#判断学分绩点
# score = eval(input("请输入分数："))
# if score >= 90:
#     gpa = 4
# elif score >= 80:
#     gpa = 3
# elif score >= 70:
#     gpa = 2
# elif score >= 60:
#     gpa = 1
# else:
#     gpa = 0
# print("应得的学分绩点为：", gpa)

#循环结构
# for
# s = 0
# for i in range(1, 101, 2):
#     s = s + i
# print("1到100的奇数和为:",s)
# help(range)

# 求一个字符串中有多少个字母o,不区分大小写
# n = 0
# str = "Life is short, You need Python!"
# for i in str:
#     if i == 'o' or i == 'O':
#         n += 1
#     else:
#         print("计算完毕。",end="")
# print("字母o的个数为：",n)


# 猜数字
# from random import randint
# n = randint(10, 100) #随机从10——100之间产生一个整数
# print("商品价格已经产生，请输入10到100之间的价格：")
# bingo = False
# while bingo == False:
#     guess = eval(input("请输入您的价格："))
#     if guess > n:
#         print("您输入的价格高于指定价格，请继续。")
#     elif guess < n:
#         print("您输入的价格低于指定价格，请继续。")
#     else:
#         print("恭喜您，猜对了，价格为：", guess)
#         bingo = True
# print("游戏结束")

#循环嵌套
#百鸡问题
#已知公鸡5元，母鸡3元，小鸡1元三只，100元怎么买
# for x in range(1,21):#假设公鸡最少买1只，最多买20只
#     for y in range(1,33):
#         z = 100 - x - y
#         if 5*x + 3*y + z/3 == 100:
#             print("公鸡",x,"母鸡",y,"小鸡",z)
# print("计算完毕")

#break 求两个数字的最小公倍数
# x = eval(input("输入第一个数字："))
# y = eval(input("输入第二个数字："))
# if x < y:
#     x,y = y,x
# for i in range(x, x*y + 1):
#     if i%x == 0 and i%y == 0:
#         print(x,"和",y,"的最小公倍数为：",i)
#         break #找到一个就直接退出

#continue 结束本次循环
# s,n = 0,0
# for i in range(1,11):
#     score = eval(input("输入成绩："))
#     if score < 60:
#         continue
#     s = s + score
#     n += 1
# print("合格人数为：",n)
# print("成绩平均值为：",round(s/n, 2))

#求四叶玫瑰数  4位自幂数
# for n in range(1000,10000):
#     a = int(n/1000)%10
#     b = int(n/100)%10
#     c = int(n/10)%10
#     d = n%10
#     if a**4 + b**4 + c**4 + d**4 == n:
#         print(n,end = ";")

#绘制菱形
# from time import sleep
# n = eval(input("输入菱形的总行数(奇数):"))
# up = int((n+1)/2)
# down = int((n-1)/2)
# for i in range(1, up+1):
#     print(" "*(up-i),end = "")
#     print("*"*(2*i-1))
# sleep(0.5)
# for i in range(1, down+1):
#     print(" "*i,end = "")
#     print("*"*(n-2*i))
# sleep(0.5)

#python 数据结构
#创建列表
# list1 = []
# print(list1)
# list2 = [1,2,3,4,5,6]
# print(list2)
# list3 = ['Python', 'C++', 'Java', 'Ruby', 'Shell']
# print(list3)
# list4 = list()
# list5 = list(range(1,10,2))
# print(list5)
# list6 = list('浙江工业大学')
# print(list6)

#列表推导式
# list1 = [x*x for x in range(1,10)]
# print(list1)
# list2 = [i for i in list1 if i%2 == 0]
# print(list2)
# list3 = [i for i in range(100,1000) if int(i/100)**3+int((i/10)%10)**3+(i%10)**3==i]#自幂数(水仙花数)
# print(list3)

#访问列表
# list1 = ['a','b','c','d','e','f']
# print(list1[0])  #a
# list1[2:4]# 三到5的元素,不包括5
# list1[-2] #逆向第二个元素 e
# list1[1:]#序列号为1到最后

#矩阵列表
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# c = [11,12,13,14,15]
# list = [a,b,c]
# print(list[1][3]) #9

#遍历二维列表
# list1 = ['20180001','小缘','女',19,'物理学院','流体力学']
# list2 = ['20180002','咬人猫','女',20,'化学工程学院']
# list3 = ['20180003','马老师','男',20,'计算机学院','计算机科学与技术','2班']
# list4 = ['20180004','有咩酱','女',19,'外语学院']
# list = [list1,list2,list3,list4]
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         print(list[i][j],end = " ")
#     print()#换行

#列表的赋值
#python中的列表也可以像变量那样进行赋值，但是要注意的是，列表的赋值只是将列表的地址进行了引用，
# 不是将实际的数据赋值给一个新表，那就意味着牵一发而动全身，一处改动，处处改动。
# list1 = ['20180004','有咩酱','女',19,'外语学院']
# list2 = list1 #地址拷贝
# list1[4] = '外国语学院'
# print(list2)

#更新列表
# fruit = ['苹果','香蕉','西瓜','桔子','桃子']
# fruit[0] = 'apple'
# fruit[-1] = 'peach'
# print(fruit)
# fruit[1:4] = ['banana','watermelon','orange']
# print(fruit)

#添加列表元素
# fruit = ['苹果','香蕉','西瓜','桔子','桃子']
# fruit.append('樱桃')
# print(fruit)
# fruit.insert(2,'柠檬')#在指定索引前插入
# print(fruit)

#删除列表元素
# fruit = ['苹果','香蕉','西瓜','桔子','桃子']
# fruit.remove('苹果')
# print(fruit)
# del fruit[:2] #del语句删除索引
# print(fruit)
# del fruit #注意，调用该语句，fruit会被完全清空，且该对象会被销毁



#元组 一旦创建，内容不可变
# tup = tuple("沈阳师范大学")
# tup1 = ()
# print(tup)
# tup2 = 1,2,3,4,5
# print(tup2)

#列表推导式
# g = (x**2 for x in range(1,10)) #返回的是一个生成器对象，使用next访问,使用后即被释放
# print(g)
# print(next(g))
# tuple1 = tuple(g)
# print(tuple1)

#访问元组
#元组当中也可以构成矩阵，如果其中包含列表元素，那么值是可以改变的
# fruit = ('苹果','香蕉','西瓜','桔子','桃子')
# print(fruit[1])

#字典
#字典创建
# dict1 = {}
# print(dict1)
# dict2 = dict([['优',90],['良',80],['中',70],['及',60]])
# dict2 = dict([('优',90),('良',80),('中',70),('及',60)])
# print(dict2)
#zip构造字典
# dict3 = dict(zip(['优','良','中','及'],[90,80,70,60]))
# print(dict3)
# dict4 = {}.fromkeys(['优','良','中','及'],'大于60分')#创建值都相同的字典
# print(dict4)

#访问字典
# dict1 = dict([['优',90],['良',80],['中',70],['及',60]])
# dict1.get('良','键不存在')
# print(dict1.items())#访问所有键值对
# dict1.keys()#访问所有的键
# dict1.values()#访问所有的值
# #for 遍历
# for i in dict1:#默认访问的是键
#     print(i,end = ", ")
# for i in dict1.values():
#     print(i,end = ",")

#添加元素
# dict1 = dict([['优',90],['良',80],['中',70],['及',60]])
# dict1.setdefault('阿西吧',50)#添加元素
# print(dict1)
# dict1.setdefault('优',0)#不会改变原值，只会返回该建的原有值
# print(dict1)

#合并字典 update
# dict1 = {'NO1':'Python','NO2':'C++'}
# dict2 = {'NO3':'Java','NO4':'VB'}
# dict1.update(dict2)# 合并两个字典，如果第二个里面与第一个键值相同会覆盖第一个

#随机产生500个小写字母，统计每个字母出现的频率
# from random import choice
# str = 'qwertyuiopasdfghjklzxcvbnm'
# dict1 = dict()
# for i in range(500):
#     r = choice(str)
#     dict1[r] = dict1.get(r,0)+1
# print('一共产生的字母为：',sum(dict1.values()))
# print('每个字母产生的词频：',dict1)

#集合
# set1 = {1,2,3,4,3,2,1}#会去除重复元素
# print(set1)
#通过set函数创建
# set1 = set()
#通过frozenset()创建不可变集合
# set2 = frozenset({1,2,3,4,5,6})
# print(set2)

#访问集合，由于集合元素是无序的，只能遍历访问
# set1 = {1,2,3,4,5,6,7}
# for i in set1:
#     print(i,end = ',')

#添加元素
# set1 = {1,2,3,4}
# set1.add(5) #添加单个元素
# set1.update({1,2,6,7})#添加多个元素

#删除元素
# set1 = {1,2,3,4}
# set1.remove(4)#删除元素4
# set1.discard(3)与remove类似，区别是如果删除的该元素不在集合内，discard不报错，remove报错
# set1.pop()#随机删除一个元素
# set1.clear()#清除所有元素


#字符串与正则表达式
#字符串的格式化  %c 字符 %s字符串  %d十进制整数 %o八进制 %x十六进制 %f浮点 %e科学计数法

#索引
# str = 'Look what you made me do'
# print(str[0],str[1],str[2])

#字符串分片操作
# st = input("输入一个字符串：")
# print('原字符串：%s'%(st))
# print('逆序字符串：%s'%(st[-1::-1]))

#字符串的运算
# s1 = 'python程序设计'
# s2 = '入门'
# n = 2
# print('%s'%(s1+s2))
# print('%s'%(s1*n))
# print(s2 in s1)
# print('a'>'A')#Ascii true


# len 返回字符串长度  ord 返回字符的ASCII  chr 返回整数的ASCII， str 将数字转成字符串

#电文加密，返回字母的后面第五个字母
# original = input('输入原文：')
# cryption = ''
# for s1 in original:
#     if s1.isalpha():
#         i = ord(s1) + 5
#         if s1.isupper():
#             if i > ord('Z'):i -= 26
#             else:
#                 if i > ord('z'):i-=26
#         s2 = chr(i)
#         cryption+=s2
#     else:
#         cryption += s1
# print('输出密文：%s'%(cryption))

#统计文章中单词出现的次数
# passage = 'Do not trouble trouble till trouble troubles you'
# word = input('input a word:')
# n = passage.count(word)
# print('%s出现的次数：%d'%(word,n))


#正则表达式re模块
# import re
# s = 'Do not trouble trouble till trouble troubles you'
# r = 't[a-zA-Z]+'
# print(re.match(r,s))#开始位置匹配
# print(re.search(r,s))#任意位置匹配
# print(re.findall(r,s))#以列表形式返回s中全部匹配的字符串

#使用split分割
# import re
# s = '210.30.208.7'
# r = re.compile('。 ')
# print(r.split(s))
# print(r.split(s,1))#按正则分割字符串，分割次数为1

#可变参数
#单星号参数，接受元组
#双星号参数，接受字典

#序列解包 支持元组 列表 字典 集合
# def square_num(* number):
#     print(number)
#     sum = 0
#     for i in number:
#         sum = sum+ i*i
#     return sum
# nums = [1,2,3]
# print(square_num(* nums))

#变量的作用域
# a,b = 3,6 #全局变量
# def fun_scope():
#     global a#声明为全局变量
#     a = 10
#     b = 20 #局部变量
#     c = a*b
#     print(a,b,c)
# fun_scope()
# print(a,b)

#函数嵌套的变量理解
# def first():
#     x1 = 'Dream1'#first函数的局部变量
#     print(x1)
#     def second(): #嵌套函数
#         x1 = 'second_dream1'#second汉书的局部变量 ，不同于first
#         global x2 #全局变量
#         x2 = 'Dream2'
#         print(x1,x2) # second_dream1 Dream2
#         def third(): #second函数的嵌套函数
#             x3 = 'Dream3'
#             print(x1,x2,x3) #second_dream1 Dream2 Dream3 优先原则
#         return third() #second的返回值为third，即调用third
#     second()
#     print(x1,x2) # Dream1 Dream2
# first()

#lambda 函数
# f = lambda x,y,z: x+y+z
# print(f(10,20,30))

#递归
#求阶乘
# def Fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*Fact(n-1)
# print(Fact(5))
# print(Fact(3))

#斐波拉契数列
# def Fib(n):
#     if n <2 :
#         return n
#     else:
#         return Fib(n-1) + Fib(n-2)
# print(Fib(5))
# print(Fib(8))

#模块
# import sys #直接导入整个模块
# print(sys.path)

#导入模块下的单个函数和整个函数
# from math import sin
# print(sin(45))
# from math import sqrt
# print(sqrt(9))
# from math import *
# print(cos(90))

#自定义模块
# import maths
# print(maths.add(5,8))


#第三方模块的导入 Pillow图像处理
# from PIL import Image
# im = Image.open('images/35440589.jpg') #打开图片
# print(im.size)

#利用turtle模块绘制多边形
# import turtle
# turtle.setup(680,280,200,200)#初始化窗口大小，宽高x,y
# turtle.pensize(5)#画笔大小
# turtle.speed(3)#速度
# turtle.color("red")
# turtle.penup()#抬起画笔
# def polygon(x,y,keep,fd,angel):
#     turtle.goto(x,y)#从当前位置画到指定位置
#     turtle.pendown()#开始画
#     for i in range(keep):
#         turtle.forward(fd)#沿当前方向画距离
#         turtle.right(angel)#转多少角度
#     turtle.penup()#抬起画笔
# polygon(-300,100,4,180,90)#正方形
# polygon(-80,100,3,200,120)#绘制三角形
# polygon(160,100,6,100,60)#六边形

#绘制圆形及曲线
# import turtle
# def circles(x,y,rad,ang=None):
#     turtle.penup()#抬起画笔
#     turtle.goto(x,y)#定位起点
#     turtle.pendown()#开始画
#     turtle.circle(rad,ang) #半径 弧度
#     turtle.penup()

# def littlesnake(x,y,loop,rad,ang):#绘制弧线
#     turtle.goto(x,y)
#     turtle.pendown()
#     for i in range(loop):
#         turtle.circle(rad,ang)
#         turtle.circle(-rad,ang)
#     turtle.penup()

# turtle.setup(680,300,200,200)
# turtle.pensize(10)
# turtle.speed(3)
# turtle.color("blue")
# circles(x=-220,y=-100,rad=100)#绘制圆形
# circles(x=-100,y=-100,rad=100,ang=180)#绘制左半圆 沿逆时针
# circles(x=100,y=-100,rad=-100,ang=180)#绘制右半圆 顺时针
# littlesnake(x=160,y=-100,loop=4,rad=20,ang=80)#水蛇


#中文分词模块 jieba
#Shirley杨  陈教授  大金牙  郝爱国 精绝古城 
#统计鬼吹灯之精绝古城中的人物出现次数，并按个数排序
# import jieba
# excludes = {"我们","什么","一个","没有","他们","就是","咱们","沙漠","但是","已经","这些","这么","东西",
# "不是","自己","不过","现在","时候","出来","可能","这种","知道","怎么","可以","这里","起来","你们",
# "精绝","古城","还有","地上","地下","地方","女王","那些","虽然","之后","还是","古墓","最后","这个"}#排除的关键字
# txt = open('鬼吹灯之精绝古城.txt', 'r', encoding = 'gbk').read()
# list1 = ["胡八一","Shirley杨","陈教授","大金牙","郝爱国","安力满","叶亦心","英子","楚健","萨帝鹏"]#人物
# #添加到分词词典
# for i in list1:
#     jieba.add_word(i)

# words = jieba.lcut(txt)#全模式解析，返回列表类型
# counts = {}#声明字典存储
# for word in words:
#     if len(word) != 1:#不统计单个汉字
#         counts[word] = counts.get(word,0)+1
# #删除去除列表当中的词
# for word in excludes:
#     del(counts[word])

# listitem = list(counts.items()) #将字典转换为可变列表
# #按列表中每个元素的第二个位置的元素的值进行降序排序
# #key指定排名前被调用的函数，reverse指定降序
# listitem.sort(key = lambda x:x[1],reverse = True)
# print("{0:<10} {1:>8}".format("人物","出场次数"))
# for i in range(10):
#     word, count = listitem[i]
#     print("{0:-<10} {1:->10}".format(word,count))


#面向对象

#类的定义
# class Person:
#     number = 0 #类属性
#     def __init__(self, name, gender, age): #类的构造函数
#         self.name = name
#         self.gender = gender
#         self.age = age
#         Person.number += 1
    
#     def displayPerson(self):
#         print('Name:',self.name,'Gender:',self.gender,'Age:',self.age)

#     def displayNumber(self):
#         print('Total person:',Person.number)

# stu1 = Person('小缘', '女', 19)
# stu2 = Person('幼儿缘', '男', 20)
# stu1.displayPerson()
# stu2.displayPerson()
# print('Total Students:',Person.number)
# stu1.displayNumber()
# stu2.displayNumber()

#属性的添加，修改与删除
# class Person:
#     number = 0 #类属性
#     def __init__(self, name, gender, age): #类的构造函数
#         self.name = name
#         self.gender = gender
#         self.age = age
#         Person.number += 1
    
#     def displayPerson(self):
#         print('Name:',self.name,'Gender:',self.gender,'Age:',self.age)

#     def displayNumber(self):
#         print('Total person:',Person.number)

# stu1 = Person('小缘', '女', 19)
# stu2 = Person('幼儿缘', '男', 20)
# stu1.score = 90
# stu2.score = 85
# stu1.displayPerson()
# stu2.displayPerson()
# print('The score of the first student:',stu1.score)
# print('The score of the second student:',stu2.score)
# stu1.age = 21
# del stu1.score #删除属性
# stu1.displayPerson()
# print('The score of the first student:',stu1.score)


#通过函数调用进行添加修改删除
# class Person:
#     number = 0 #类属性
#     def __init__(self, name, gender, age): #类的构造函数
#         self.name = name
#         self.gender = gender
#         self.age = age
#         Person.number += 1
    
#     def displayPerson(self):
#         print('Name:',self.name,'Gender:',self.gender,'Age:',self.age)

#     def displayNumber(self):
#         print('Total person:',Person.number)

# stu1 = Person('小缘', '女', 19)
# stu2 = Person('幼儿缘', '男', 20)
# setattr(stu1,'score',90) #修改属性,score是对象属性
# print(getattr(stu1,'score'))#获取属性
# print('The score of the first student:',stu1.score)
# delattr(stu1,'score')#删除属性
# print(hasattr(stu1,'score'))#如果存在属性，则返回True

#公有属性与私有属性 ，私有属性前面有__
# class Car:
#     salesPrice = 150000 #类属性
#     __manufacturePrice = 120000 #私有类属性
#     def __init__(self, brand, serial):
#         self.brand = brand
#         self.__serial = serial #私有对象属性

# print('公有属性salesPrice：',Car.salesPrice)
# print('私有数据manufacturePrice',Car._Car_manufacturePrice) #私有属性使用className_className._私有属性
# c1 = Car('大众', '甲壳虫')
# print('c1的公有属性brand:',c1.brand)
# print('c1的私有属性serial:',c1._Car_serial) #私有对象属性 实例化对象._className_私有对象


#公有方法与私有方法的调用
# class Methods:
#     def publicMethod1(self): #公有方法,直接通过类调用
#         print('公有方法publicMethod!')
    
#     def __privateMethod(self): #私有方法，通过类名调用传入实例化对象调用，或者对象._className__方法()
#         print('私有方法privateMethod!')
    
#     def publicMethod2(self):
#         self.__privateMethod()

# m = Methods()
# m.publicMethod1()#通过对象调用公有方法
# Methods.publicMethod1(m) #类名调用公有方法
# m.publicMethod2()#通过公有方法调用私有方法
# m._Methods__privateMethod()#通过对象名调用私有方法
# Methods._Methods__privateMethod(m) #通过类名调用


#类方法  @classmethod 或者classmethod()
# class Methods:
#     @classmethod
#     def publicClassMethod(cls): #公有类方法
#         print('公有类方法publicClassMethod!')
    
#     @classmethod
#     def __privateClassMethod(self): #定义私有类方法
#         print('私有类方法privateClassMethod!')

#     def publicMethod(self):
#         print('普通公有方法publicMethod!')

#     def __privateMethod(self):
#         print('普通私有方法privateMethod!')

#     publicMethodToClassMethod = classmethod(publicMethod) #转换为类方法
#     privateMethodToClassName = classmethod(__privateMethod)

# m = Methods()
# m.publicClassMethod()
# Methods.publicClassMethod()
# m._Methods__privateClassMethod()
# Methods._Methods__privateClassMethod()
# m.publicMethodToClassMethod()
# Methods.publicMethodToClassMethod()
# m.privateMethodToClassName()
# Methods.privateMethodToClassName()


#静态方法
# class Methods:
#     @staticmethod #公有静态方法
#     def publicStaticMethod():
#         print('公有静态方法publicStaticMethod!')

#     @staticmethod
#     def __privateStaticMethod():
#         print('私有静态方法privateStaticMethod!')

#     def publicMethod(self):
#         print('普通公有方法publicMethod!')

#     def __privateMethod(self):
#         print('普通私有方法privateMethod!')

#     publicMethodToStaticMethod = staticmethod(publicMethod)
#     privateMethodToStaticMethod = staticmethod(__privateMethod)

# m = Methods()
# m.publicStaticMethod()
# m._Methods__privateStaticMethod()
# Methods._Methods__privateStaticMethod()
# m.publicMethodToStaticMethod(m) #静态方法需要传入对象
# Methods.publicMethodToStaticMethod(m)
# m.privateMethodToStaticMethod(m)
# Methods.privateMethodToStaticMethod(m)


#析构函数 __del__()
# class Person:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age
        
#     def __del__(self):
#         print('调用析构函数:',self.name, self.gender, self.age)

# stu1 = Person('小缘', '女', 19)
# stu2 = Person('幼儿缘', '男', 20)
# print('Name:',stu1.name,'Gender:',stu1.gender,'Age:',stu1.age)
# print('Name:',stu2.name,'Gender:',stu2.gender,'Age:',stu2.age)
# del stu1
# del stu2

#派生类的定义
# class Person:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def display(self):
#         print('Name:',self.name,'Gender:',self.gender,'Age:',self.age)

#派生类
# class Student(Person):
#     def __init__(self, num, major, name, gender, age):
#         Person.__init__(self, name, gender, age) #调用基类构造函数
#         #派生类新增属性
#         self.num = num
#         self.major = major

#     def displayStudent(self):
#         print('Number:',self.num,'Major:',self.major)
#         Person.display(self) #调用基类方法

# stu1 = Student('201802181','计算机科学与技术','小缘', '女', 19)
# stu2 = Student('201810050', '外国语', '幼儿缘', '男', 20)
# stu1.displayStudent()
# stu2.displayStudent()

#内置函数super()的使用
# class Person:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def display(self):
#         print('Name:',self.name,'Gender:',self.gender,'Age:',self.age)

# class Student(Person):
#     def __init__(self, num, major, name, gender, age):
#         super(Student, self).__init__(name, gender, age)#调用基类
#         self.num = num
#         self.major = major
    
#     def displayStudent(self):
#         print('Number:',self.num,'Major:',self.major)
#         super(Student, self).display()#调用基类方法

# stu1 = Student('201802181','计算机科学与技术','小缘', '女', 19)
# stu2 = Student('201810050', '外国语', '幼儿缘', '男', 20)
# stu1.displayStudent()
# stu2.displayStudent()


#多继承
# class Student():
#     def __init__(self, num, name, gender):
#         self.num = num
#         self.name = name
#         self.gender = gender

#     def displayStudent(self):
#         print('学号:%s,姓名:%s,性别:%s'%(self.num, self.name, self.gender))

# class Teacher():
#     def __init__(self, title, major, subject):
#         self.title = title
#         self.major = major
#         self.subject = subject

#     def displayTeacher(self):
#         print('职称:%s,专业:%s,课程:%s'%(self.title, self.major, self.subject))

# class Assistant(Student, Teacher):
#     def __init__(self, num, name, gender, title, major, subject, salary):
#         Student.__init__(self, num, name, gender)
#         Teacher.__init__(self, title, major, subject)
#         self.salary = salary

#     def displayAssistant(self):
#         super(Assistant, self).displayStudent()
#         super(Assistant, self).displayTeacher()
#         print('工资',self.salary)

# ta = Assistant('20150709', '幼儿缘', '女', '助教', '软件工程', '程序设计', 800)
# ta.displayAssistant()


##多态性  方法重载
# class Animal():
#     def display(self):
#         print('I am an animal.')

# class Dog(Animal):
#     def display(self):
#         print('I am a Dog!')

# class Cat(Animal):
#     def display(self):
#         print('I am a cat!')

# class Wolf(Animal):
#     def display(self):
#         print('I am a wolf.')

# x = [item() for item in (Animal, Dog, Cat, Wolf)] #列表推导式生成列表
# for item in x:
#     item.display()

#运算符重载
# class Number():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, x): #重载加号
#         return Number(self.a + x.a, self.b + x.b)

#     def __sub__(self, x):#重载减号
#         return Number(self.a - x.a, self.b - x.b)

# n1 = Number(10, 20)
# n2 = Number(100, 200)
# m = n1 + n2
# n = n2 - n1
# print(m.a, m.b)
# print(n.a, n.b)


#文件处理

#文件的打开与关闭
# try:
#     fh = open('test.txt','w')
#     fh.write("武田华恋 小缘\n")
#     fh.write("萌萌哒!")
# except IOError:
#     print('Error: 没有找到文件或文件读取失败')
# finally:
#     print('文件写入成功')
#     fh.close()

#文件读取
#read()函数 可以一次性全部读出，可以指定每次读取的字节数
# f = open('test.txt','r')
# fcontent = f.read()
# print(fcontent)
# f.seek(0) #位置移动到文件头
# fcon = f.read(7) #从文件头开始读取7个字节
# print(fcon)
# f.close()


#readline()函数，每次只读取一行数据,可以指定字节数
# f = open('test.txt','r')
# fcontent = f.readline()
# print(fcontent)
# fcon = f.readline(6)
# print(fcon)
# f.close()


#readlines()函数，读取当前指针后面的所有内容，以列表形式返回，需要遍历
# f = open('test.txt','r')
# fcontent = f.readlines()
# for oneline in fcontent:
#     print(oneline)
# f.close()

#文件写入
#write()函数
# f = open('test.txt','w+')
# f.write('永远讲不完的故事')
# f.write('\n')
# f.write('はてしない物語')
# f.seek(0)#定位到开始
# fc = f.read()
# print(fc)
# f.close()

#writelines()将列表内容写入文件
# f = open('test.txt','w+')
# writeList = ['永远讲不完的故事\n', 'はてしない物語']
# f.writelines(writeList)
# f.seek(0)
# fc = f.read()
# print(fc)
# f.close()


#文件指针定位函数seek(偏移量, 起始点)   基点 1表示文件头 2表示文件尾部
# f = open('test.txt','w+')
# strList = ['abc', 'def', 'ghi']
# f.writelines(strList)
# f.seek(0)
# fc1 = f.read(1) #读一个字符 a
# print(fc1)
# f.seek(0,1) #指向当前位置，偏移量为0
# fc2 = f.read(1) #读取b
# print(fc2)
# f.seek(5)
# fc3 = f.read(1)# f
# print(fc3)
# f.seek(0,2) #移动到末尾
# f.write('xyz')
# f.seek(0)
# fc = f.read()
# print(fc)
# f.close()


# tell()函数 获取当前文件指针的位置，用相对于文件头的偏移量表示
# f = open('test.txt', 'w+')
# strList = ['abc', 'def', 'ghi']
# f.writelines(strList)
# print('当前位置指针：', f.tell()) #9
# f.seek(0)
# print('当前位置指针:',f.tell()) #0
# fc1 = f.read(1)
# print(fc1)
# f.seek(0,1)  #1
# print('当前位置指针:',f.tell())
# fc2 = f.read(1)
# print(fc2)
# f.seek(5) #移动到文件头后的第五个字符
# print('当前位置指针:',f.tell())
# fc3 = f.read(1)
# print(fc3)
# f.seek(0,2)
# print('当前指针:',f.tell())
# f.write('xyz')
# f.seek(0)
# print('当前位置指针:',f.tell())
# fc = f.read()
# print(fc)
# f.close()

# os模块

#文件的删除
# import os
# filename = 'test.txt'
# isExist = os.path.exists(filename)
# if isExist:
#     os.remove(filename)
#     print('文件删除成功！')
# else:
#     print('所要删除的文件不存在!')


#文件夹的创建
# import os
# dirname = 'E:/test'
# multipledirname = 'E:/test/python/program'
# isExist = os.path.exists(dirname)
# if isExist:
#     print(dirname, '文件夹已存在')
# else:
#     os.mkdir(dirname) #创建目录
#     print('成功创建一级目录文件夹')
# isExist = os.path.exists(multipledirname)
# if isExist:
#     print('multipledirname','文件夹已存在')
# else:
#     os.makedirs(multipledirname)#创建多级目录
#     print('成功创建多级目录文件夹')

#文件夹的删除
# import os
# import shutil
# dirname = 'E:/test/python'
# isExist = os.path.exists(dirname)
# if isExist:
#     shutil.rmtree(dirname) #该方法可以删除非空文件夹  rmdir()只能删除空文件夹
#     print('成功删除非空文件夹!')
# else:
#     print('文件夹不存在!')


#异常处理
#常见异常  除零错误(ZeroDivisionError) 变量名错误(NameError) 操作数类型错误(TypeError)
# 下标越界错误(IndexError) 打开文件错误(FileNotFoundError) 语法错误(SyntaxError)

# try...except...语句
# a = [1,2,3,4,5]
# try:
#     print(a[5])
# except IndexError:
#     print('索引下标越界')

#try...except...else
# while True:
#     try:
#         x = int(input('请输入数据1:'))
#         y = int(input('请输入数据2:'))
#         z = x/y
#     except ValueError:
#         print('应全部输入数值数据!')
#     else:
#         print('最终结果为:',z)
#         break

#多种异常
# while True:
#     try:
#         x = eval(input('请输入数据1:'))
#         y = eval(input('请输入数据2:'))
#         z = x/y
#     except ValueError:
#         print('应全部输入数字!')
#     except ZeroDivisionError:
#         print('除数不能为0')
#     except NameError:
#         print('变量不存在')
#     else:
#         print('最终结果为:',z)
#         break
#     finally:
#         print('END')


#断言与上下文管理语句

#断言
# try:
#     x = int(input('请输入数据1:'))
#     y = int(input('请输入数据2:'))
#     s = '两次输入数据不相等'
#     assert x == y, s #s作为except的实例传入
# except AssertionError:
#     print(s)


#上下文管理语句 执行前期或收尾工作
# e.g.文件读写模块使用上下文操作无需进行关闭操作
# with open('hello.txt','w') as f:
#     f.write('Hello')
#     f.write('Python')


#python 高级编程

#GUI编程  tkinter

#first gui examp
# import tkinter
# top = tkinter.Tk()#顶层窗口
# label1 = tkinter.Label(top, text = '幼儿缘')
# label1.pack()#放置
# top.mainloop()#进入事件循环


#pack布局
# import tkinter
# top = tkinter.Tk()
# top.geometry('320x120+0+0')
# label1 = tkinter.Label(top, text = '扬州')
# label2 = tkinter.Label(top, text = '杭州')
# label3 = tkinter.Label(top, text = '苏州')
# label4 = tkinter.Label(top, text = '长安')
# label1.pack(side = 'left', fill = 'both')
# label2.pack(side = 'right', fill = 'both', padx = 5, pady = 3)
# label3.pack(side = 'top', fill = 'x', expand = 'yes', anchor = 'n')
# label4.pack(side = 'bottom', expand = 'yes', anchor = 's')
# top.mainloop()

#文字标签
# import tkinter
# root = tkinter.Tk()
# root.geometry('300x100+0+0')
# root.wm_title('标签组件实例')
# label1 = tkinter.Label(root, text = '幼儿缘', height = 4 ,width = 20, relief = 'ridge', background = '#fff',\
#                        anchor = 'center', font = '黑体', cursor = 'man')
# label1.grid(row = 0, column = 1, padx = 60)
# root.mainloop()


#图像标签
# import tkinter
# root = tkinter.Tk()
# root.geometry('1600x1066+0+0')
# root.wm_title('图像标签示例')
# x = tkinter.PhotoImage(file = '35440589.jpg')
# label1 = tkinter.Label(root, image = x, height = 1066, width = 1600, relief = 'ridge')
# label1.pack()
# root.mainloop()

#TCP编程  socket(family, type)
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect('www.baidu.com', 80)# 建立连接  地址与端口号
# s.send("内容")
# buf = []
# while True:
#     d = s.recv(1024) #接收数据以及每次接收的数据量
#     if d:
#         buf.append(d)
#     else:
#         break
# data = 


#TCP服务器编程实例
# import socket
# import sys
# HOST = '127.0.0.1'
# PORT = 5000
# s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
# print('Socket绑定端口成功')
# s.listen(5) #连接的最大数量
# print('Socket开始监听')
# while True:
#     conn,addr = s.accept()#接收新连接
#     print('Connected with'+addr[[0]+':'+str(addr[1]))
#     #创建新的线程处理TCP连接:
#     t = threading.Thead(tcplink, args=(sock,addr))
#     t.start()


# def tcplink(sock, addr):
#     print('请输入新的连接%s:%s...' %addr)
#     sock.send(b'welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
# sock


#UDP编程
#服务端
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
# s.bind(('127.0.0.1', 10021))
# print('UDP连接')
# while True:
#     data,addr = s.recvfrom(1024)
#     print('收到数据 %s:%s.' %addr)
#     s.sendto(data.decode('utf-8').upper().encode(),addr) #将数据送回客户端

# #客户端
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
# addr = ('127.0.0.1', 10021)
# while True:
#     data = input('请输入要处理的数据:')
#     if not data or data == 'quit':
#         break
#     s.sendto(data.encode(),addr)
#     recvdata,addr = s.recvfrom(1024)
#     print(recvdata.decode('utf-8'))
# s.close()

#python网络爬虫
#使用requests库
# import requests
# URL = 'http://ip.taobao.com/service/getIpInfo.php'
# try:
#     r = requests.get(URL, params={'ip':'8.8.8.8'}, timeout = 1)
#     r.raise_for_status() #入国响应状态码不是200，主动抛出异常
# except requests.RequestException as e:
#     print(e)
# else:
#     result = r.json()
# print(type(result), result, sep = '\n')


#html解析库beautifulsoup4
#抓取淘宝网首页分类
# import requests
# from bs4 import BeautifulSoup
# r = requests.get('http://www.taobao.com')
# r.encoding = 'utf-8'
# soup = BeautifulSoup(r.text, "html.parser")
# for list in soup.find_all('a'):
#     if not list.string == None:
#         print(list.string)


#抓取糗事百科的热门段子
# import requests
# from bs4 import BeautifulSoup
# content = requests.get("http://www.qiushibaike.com").content
# soup = BeautifulSoup(content, 'html.parser')
# for div in soup.find_all('div',{'class':'content'}):
#     print(div.text.strip())


#sqlite数据库操作
import sqlite3
conn = sqlite3.connect('school.db')#连接数据库school.db
cursor = conn.cursor() #打开游标
print('数据库已打开!')
#创建表
cursor.execute('''create table student(ID int primary key not null,
                 Name text not null,Age int not null,Score real,Address char(50)) ''')
print('创建表成功!')
#插入记录
cursor.execute("insert into student values(1001,'小缘',20,589,'辽宁沈阳')")
cursor.execute("insert into student values(1002,'幼儿缘',19,568,'江苏扬州')")
conn.commit()
for row in cursor.execute('select * from student'):
    print(row)
conn.close()