# -*- coding: UTF-8 -*-


#学习参照：http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
#廖雪峰的官网，非常感谢你的分享！


#Python 中文编码:  # -*- coding: UTF-8 -*-
# 输入输出print 和 raw_print
abc=123
print abc
name=raw_input("请输入一个名字：")
print "您输入的名字是：",name

#单行注释
"""
多行注释
"""

"""
数据类型和变量
数据类型：整数、浮点数、字符串、布尔、空值
变量：变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
等号”=“是赋值符号
常量：所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
"""
PI=123
print PI

#Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换：
print 'A的数字值的是:',ord('A')
print '65代表字母是:',chr(65)

print u'中文测试'


#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
#用len()函数可以获得list元素的个数
classname=['maomao','spy','syr','spl','cjs']
print '学生有：',len(classname),'个'

print '分别是：'
for name in classname:
	print name,
#list是一个可变的有序表，所以，可以往list中追加元素到末尾：append（）
print '原来的学生名字：',classname
classname.append('sxm')
print '现在的学生名字：',classname

#也可以把元素插入到指定的位置，比如索引号为1的位置：insert
classname.insert(1,'111')
print 'insert后的学生名字：',classname

#要删除list末尾的元素，用pop()方法：
classname.pop()
print 'pop后的值是：',classname

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classname.pop(2)
print 'pop(i)后的值是：',classname

#条件判断和循环
"""
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
"""
age=33
if age<20:
	print "小孩"
elif age<50:
	print "成年人"
else:
	print "老人"

"""
第一种循环for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
"""
imgs=('1','2','3','4','5','6','7','8')
for img in imgs:
	print img,

"""
第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
"""
n,sum=0,0
while n<=10:
	sum=sum+n
	n=n+2
print "总数为：",sum

#使用dict和set
dic={'name':'maomao','age':25,'tel':18260346208}
print dic['age']

  
#调用函数  http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738355709946f704395994738a02e64a890af576f000









