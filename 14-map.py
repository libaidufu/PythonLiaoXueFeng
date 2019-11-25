'''
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
def f(x):
	return x * x

# 传入的f是函数对象本身
# r本身是一个map对象，即map函数返回的是map对象本身
r = map(f, [1,2,3,4,5,6,7,8,9])
# print(r)     # <map object at 0x10c185940>
print(list(r))


# L = []
# for n in [1,2,3,4,5,6,7,8,9]:
# 	L.append(f(n))
# print(L)
#
# st = list(map(str,[1,2,3,4,5,6,7,8,9]))
# print(st)



