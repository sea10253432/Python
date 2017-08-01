# _*_ coding: utf-8 _*_

# 转义字符练习
# \t tab
tabby_cat = "\tI'm tabbed in."
# \n 换行
persian_cat = "I'm split \non a line."
# \\ 显示'\'字符
backslash_cat = "I'm \\ a \\ cat."

# 三引号制作一个列表
fat_cat = """
I'll do a list:
\t* Cat food
\t* 'Fishies'
\t* Catnip \n\t* Grass
"""

# 打印字符串
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# %r 打印出来的是你作为程序员写在脚本里的东西，而%s 打印的是你作为用户应该看到的东西

print tabby_cat * 3
print "persian_cat %s" % persian_cat
print "persian_cat %r" % persian_cat
