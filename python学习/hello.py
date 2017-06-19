# coding=utf-8

# 输入输出print 和 raw_print
abc=123
print abc
name=raw_input("请输入一个名字：")
print "您输入的名字是：",name

#数据类型和变量
#数据类型：整数、浮点数、字符串、布尔、空值
#变量：变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
#等号”=“是赋值符号
#常量：所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
abc = 100
if abc > 10:
	print "冒冒"
else:
	print "set"
PI=123
print PI

#Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换：

print 'A的数字值的是:',ord('A')
print '65代表字母是:',chr(65)

print u'中文测试'


#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素

