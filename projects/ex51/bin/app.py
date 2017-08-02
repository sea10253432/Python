-- coding:utf-8 --
import web
# web 框架，此处是安装了 lpthw.web,是 web.py 的某个锁定版本，到 http://webpy.org 阅读文档

urls = (
	'/hello', 'Index'
)
# 小括号代表 urls 是 tuple 元组数据类型，元组是一种不可变序列
# 中括号代表 list 列表数据类型，是一种可变序列
# colors = ['yellow','blue','red']
# 花括号（大括号）代表 dict 字典数据类型，
# areaCode = {'杭州':'0571','上海':'021','南京':'025}

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def Get(self):
		form = web.input(name="Nobody")
		greeting = "hello, %s" % form.name
		
		return render.index(greeting = greeting)
		
if __name__ == "__main__":
	app.run()
	