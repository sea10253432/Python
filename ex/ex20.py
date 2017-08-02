from sys import argv

script, input_file = argv

# 定义 print_all 函数，打印文件内容
def print_all(f):
	print f.read()
	
# 定义 rewind 函数：操作文件的指针回到文件的开头位置。    
def rewind(f):
	f.seek(0)
	
# 定义 print_a_line 函数，从文件中读取一行，然后打印内容
def print_a_line(line_count, f):
	print line_count, f.readline()
	
# 打开 input_file 文件，文件对象赋值给 current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# 读取文件所有内容，打印出来
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# 读写文件的指针回到文件的开头位置
rewind(current_file)

print "Let's print three lines:"

# 设置文件当前行为1
current_line = 1
# 读取文件当前行内容，打印内容
print_a_line(current_line, current_file)

# 文件当前行数+1
current_line = current_line + 1
# 读取文件当前行内容，打印内容
print_a_line(current_line, current_file)

# 文件当前行数加1
current_line = current_line + 1

# 读取文件当前行内容，打印内容
print_a_line(current_line, current_file)


		