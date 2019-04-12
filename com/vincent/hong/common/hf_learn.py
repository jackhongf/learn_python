from com.vincent.hong.service.hf_utils import *
#*************************************************基本数据类型篇****************************************************
#python 的六种数据类型 string、number、list、dict、set、元组， 其中 string、number、元组 是不可变得 ，其他的是可变得。
#string
a="hello python"
    #------------------
print("string:"+a)

#number  ：int ，float，complex ，
b=23.2
b1=complex(12,32)
b2=complex(23.2323,42323)
b3=complex(23.2323,0)
#------------------
b+=12
print("number:",b)
print("number complex:",b1)
print("number complex b1+b2:",b1+b2)
print("number complex b1*b2:",b1*b2)
print("number complex b3:",b3)


#list
c=[]
#------------------
c.append("sdfsd")
c.append("2324")
c.append("3452")

print("list:",c)

#dict 字典
d={}
#------------------
d['sdf']=12
print("dict:",d)

#set
e=set()
e.add("1")
e.add("2")
#------------------
print("set:",e)

#tuple 元组
f=("23",2)
print("tuple:",f)

##*************************************************基本语法篇***********************************************************
#四则运算
num1=23.0
num2= 343
print("加法 add1+add2:",num1+num2)
print("减法 add1-add2:",num1-num2)
print("乘法 add1*add2:",num1*num2)
print("除法 add1/add2:",num1/num2)
print("除法取整 num2//num1:",num2//num1) #如果除数或被除数存在小数的情况，得出的结果小数点后一位 0

#逻辑判断
flag = True

#if 判断
if flag:
    print("这是一个真的：",flag)
else:
    print("这是一个假的：",flag)

#for循环
for i in c:
    print("list c :",i)

#while循环
count =0
total=len(c)
while count< total:
    print("遍历开始：",count,c[count])
    pass
    count+=1
print("遍历结束！！！！！！")


def printObj(str):
    print("输出结果为:",str)



#迭代器
it=iter(c)
for x in it:
    printObj(x)
    pass

printObj("----------------------------------------------------")


import  time
now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(now)




#GUI 界面
#import tkinter
#top=tkinter.Tk()
#top.wm_title("这是一个GUI界面")
#top.mainloop()

word =10
def test(name,age,gender):
    global word
    word+=word
    print("name:",name)
    print("age:",age)
    print("gender:",gender)
    print("word:",word)

test(age=10,gender=20,name="jack")

print(addNum(13,34))

money=23


# strs=input("您的输入是：")
# printObj(strs)


class MyException(RuntimeWarning):
    def __init__(self,arg):
        self.args(arg)



text=open("H:\word.txt",mode='a+')
try:
    for er in range(1,100000):
        text.write(str(er))
        text.write("\r")
        pass
except (IOError,SystemError):
    printObj("io exception")
else:
    printObj("文件追加结束")
finally:
    printObj("try  except finally 最后结果")
    text.flush()
    text.close()
    #测试自定义异常
    # raise MyException("测试自定义异常")


#一个简单的网络爬虫
"""
from urllib import request
url= "https://github.com/"
response=request.urlopen(url)
html =response.read()
files=open("H:\word122.html",mode='wb+')
files.write(html)
printObj(html)
printObj(MyException.__doc__)
"""

class User:
    #双 '_' 代表类的成员变量为private
    __nameVal='jack'
    #单'_' 代表类成员变量为 protected
    _ageVal=12
    #成员变量为类public
    publicGenderVal='F'
    #这是一个默认的构造器
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    #这是一个构造器自定义构造器，直接通过对象调用
    # self： 代表对象实例本身
    # cls： 代表类本身
    @classmethod
    def invokeUser(cls):
        pass
        return cls



def testCreateObj():
    user = User(name='jack' ,age=23,gender='F')
    print(user.publicGenderVal)
    print(user.gender)

"""
    if hasattr(user, 'name'):
        setattr(user, 'name', 'rose')
        printObj("设置名称成功：rose")
        pass
"""
testCreateObj()

class House(object):
    __name=''
    __address=''
    __floor=0
    __heigth=0
    __prise=0

    def __int__(self):
        print("我是父类：House")

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getFloor(self):
        return self.__floor

    def getHeigth(self):
        return self.__heigth

    def getPrise(self, prise):
        return self.__prise

    def setHeigth(self,heigth):
         self.__heigth=heigth

    def setPrise(self,prise):
         self.__prise=prise

    def setName(self,name):
         self.__name=name

    def setAddress(self,address):
         self.__address=address

    def setFloor(self,floor):
         self.__floor=floor

    def toString(self):
        dit={}
        dit["__name"] = self.__name
        dit["__address"] = self.__address
        dit["__floor"] = self.__floor
        dit["__heigth"] = self.__heigth
        dit["__prise"] = self.__prise
        return str(dit)


class School(House):
    def __int__(self):
        print("我是子类 School")

def testHouse():
    house = House()
    house.setAddress("武汉")
    house.setFloor(10)
    house.setHeigth(200)
    house.setName("保利新武昌")
    house.setPrise(720000)
    print(house.toString())
    chd = School()
    chd.getHeigth()

testHouse()


# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="mysql",  # 数据库密码
#     database = "python"
#
# )
# myCursor = mydb.cursor()
# sql="insert into User (name,address,gender)values (%s,%s,%s) "
# val=('jack','武汉','F')
# myCursor.execute(sql,val)
# mydb.commit()
# print("插入用户成功")

"""
import pymysql
db=pymysql.connect("localhost","root","mysql","python")
cursor=db.cursor()
sql="select * from User"
cursor.execute(sql)
results=cursor.fetchall()
for tmp in results:
    id=tmp[0]
    name=tmp[1]
    address=tmp[2]
    gender=tmp[3]
    printObj(tmp)
    print("id=%s,name=%s,address=%s,gender=%s"%(id,name,address,gender))
sql="insert into User (name,address,gender)values (%s,%s,%s) "
val=('mark','天津','F')
# insertSql=r"insert into User(name,address,gender) values('rose','上海','M')"
cursor.execute(sql,val)
db.commit()
"""
import re
import datetime
def calculateDate(startDateStr,endDateStr):

    reg="^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$"
    formart="%Y-%m-%d %H:%M:%S"
    if not re.match(reg,startDateStr):
        raise RuntimeWarning("时间格式错误")

    if not re.match(reg,startDateStr):
        raise RuntimeWarning("时间格式错误")

    startDate=datetime.datetime.strptime(startDateStr,formart)
    endDate=datetime.datetime.strptime(endDateStr,formart)
    compareYear =endDate-startDate
    days=compareYear.days
    year=days//365
    years=days/365
    month=((years-year)*12)
    printObj("相差"+str(year)+"年"+str(month)+"月" )

calculateDate('2014-08-15 00:00:00','2019-04-12 23:59:59')




