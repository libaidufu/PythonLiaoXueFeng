# 类名一般是大写开头的字母
class Student(object):
	"""docstring for Student"""
	# self本身也是传入函数内部的参数，即实例(instance)本身
	# 一般来说，函数，包括类内部的方法，只可以使用函数内部的变量和传入函数内部的参数，一般不使用全局变量
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s : %s ' % (self.name, self.score))

bart = Student('bart', 59)
lisa = Student('lisa', 78)
bart.print_score()
lisa.print_score()

print(bart.name)
bart.score=89
print(bart.score)


'''
私有数据成员

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__

在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

所以，我们把Student类改一改：
'''
class Student2(object):
	"""docstring for Student"""
	# self是类内部方法默认的函数参数
	def __init__(self, name, score):
		self._Student2__name = None
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s : %s ' % (self.__name, self.__score))
	def get_name(self):
		return self.__name

bartt = Student2('bart', 59)
bartt.print_score()
# 创建了一个新的数据成员
bartt.swecore = 89
bartt.__init__('libai',90)
bartt._Student2__name = 'nihk'
bartt.print_score()
# print(bartt.swecore)
# print(bartt.get_name())
'''
双下划线开头的实例变量是不是一定不能从外部访问呢？

其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name

所以，仍然可以通过_Student__name来访问__name变量：
'''

# print(bartt._Student2__name)