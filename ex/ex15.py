# -*- coding: utf-8 -*-

from sys import argv

script ,filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close

#读取文件名称
#print "Type the filename again:"
file_again = raw_input("> ")

#打开txt_again文件
txt_again = open(file_again)

# 将txt_again文件读取并打印出来
print txt_again.read()

txt_again.close