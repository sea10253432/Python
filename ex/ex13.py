# _*_ coding: utf-8 _*_

# import argv 模块，第一个参数是脚本文件名称，此处为 ex13.py， 运行脚本的时候依次输入其他3个参数，不同参数之间用空格分开。
from sys import argv

# 将 argv 解包（unpack），含义：把 argv 中的内容解包，所有的参数依次赋值给左边的这些变量，变量个数必须符合
# script, first, second, third = argv

script = argv[0]
# script, first = argv
first = raw_input("First variable:")
second = raw_input("Second variable:")
third = raw_input("Third variable:")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

