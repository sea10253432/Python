# -*- coding: utf-8 -*-
# 从sys 导入 argv 模块
from sys import argv

# 解包运行该脚本时的参数，将所有的参数依次赋值给左边的变量
script ,filename = argv

# 打开文件，返回的文件对象赋值给 txt
txt = open(filename)

# 打印打开的文件名
print "Here's your file %r:" % filename

# 读取文件对象的内容，然后打印
print txt.read()

# 关闭文件对象
txt.close

#从终端获取文件名称
#print "Type the filename again:"
file_again = raw_input("> ")

#打开终端输入的文件名称，返回的文件对象赋值给 txt_again
txt_again = open(file_again)

# 读取文件对象的内容并打印出来
print txt_again.read()

# 关闭文件
txt_again.close

