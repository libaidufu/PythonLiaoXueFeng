'''
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
'''
# def calc_num(*args):
# 	ax = 0
# 	for n in args:
# 		ax = ax + n
# 	return ax
#
# print(calc_num(12,23,43))

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
# def lazy_sum(*args):
# 	def sum():
# 		ax = 0
# 		for n in args:
# 			ax = ax + n
# 		return ax
	# 返回一个函数对象不能是sum()，这是表示先执行函数，然后返回的是函数的返回值
	# return sum()
	# 返回sum表示返回的是函数本身
	# return sum
	# 无法返回局部变量
	# return ax

# f = lazy_sum(23,43,545,23)
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
# 打印一个函数和打印一个函数的返回值是不同的
# a1 = [1,2,3]
# print(a1)
# print(f)
# 调用函数f时，才真正计算求和的结果：
# print(f())


'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''
# def count():
# 	fs = []
# 	# range索引是前开后闭
# 	for i in range(1, 4):
# 		def f():
# 			return i * i
# 		# 将f加入到了fs这个列表中，f是函数对象，并且该函数对象并没有被执行，并不是执行函数后的返回值f()
# 		fs.append(f)
# 	# 整个for循环结束之后，才执行return语句，而return语句中列表中的每一个函数并没有执行，函数内部的i会一直变化，并等于最终的循环变量的值
# 	return fs
# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 这一步对list进行了拆分，相当于解压序列赋值给多个对象。即count()是一个列表
# f1,f2,f3 = count()
# print(f1(),f2(),f3())
# f4 = count()
# print(f4[0]())

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
	return fs

f1,f2,f3 = count()
print(f1(),f2(),f3())