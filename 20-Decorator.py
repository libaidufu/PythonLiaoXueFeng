
'''
假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''
#因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
def log(func):
	def wrapper(*args, **kw):
		print('现在在调用 %s():' % func.__name__)
		#  从下面这一步可以看出func是一个函数，否则不可能有输入参数
		return func(*args, **kw)
	# 一个装饰器的返回值是一个函数
	return wrapper



# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
	print('2015-3-25')

f = now
# 运行这个函数，相当于动态增加了函数功能
# f()

@log
def now2():
	return '2015-43-2'

f = now2
# f()
# 下面这两个打印不一样，print(f)只是打印f这个对象的属性，print(f())首先会执行函数f()，再打印函数f执行后的返回值
# print(f)
# print(f())

# 函数对象有一个__name__属性，可以拿到函数的名字
# nowv只是命名空间的一个变量名，经过装饰器后，now指向了新的函数对象
print(now.__name__)        # 返回wrapper
print(f.__name__)          # 返回wrapper


'''
把@log放到now()函数的定义处，相当于执行了语句：

now = log(now)

由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
'''

'''
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。

比如，要自定义log的文本：
'''
# def log(text):
# 	def decorator(func):
# 		def wrapper(*args, **kw):
# 			print('%s %s():' % (text, func.__name__))
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorator
#
# @log('execute')
# def now():
# 	print('balabala')
#
# now()


'''
和两层嵌套的decorator相比，3层嵌套的效果是这样的：

>>> now = log('execute')(now)

我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
'''


# import functools
#
# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print('call %s():' % func.__name__)
# 		return func(*args, **kw)
# 	return wrapper
