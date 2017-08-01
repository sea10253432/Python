# _*_ coding: utf-8 _*_

# 为格式化字符串变量赋值
formatter = "%r %r %r %r"

# 格式化打印数字
print formatter % (1, 2, 3, 4)
# 格式化打印字符串
print formatter % ("one", "two", "three", "four")
# 格式化打印布尔变量
print formatter % (True, False, False, True)
# 格式化打印格式化字符串
print formatter % (formatter, formatter, formatter, formatter)
# 打印结果4个字符串，第1、2、4三个字符串显示单引号，第3个字符串显示为双引号，对于%r，打印参数，Python 会用最有效的方式打印出字符串，第3个支付串内容包含’符号，此时用单引号会引发歧义，因此使用双引号
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
