# _*_ coding: utf-8 _*_

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# 字符串赋值
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# 打印字符串
print joke_evaluation % hilarious

# 给字符串变量 w 赋值
w = "This is the left side of..."

# 给字符串变量 e 赋值
e = "a string with a rihht side."

# 连接字符串 w 和字符串 e，然后打印
print w + e

