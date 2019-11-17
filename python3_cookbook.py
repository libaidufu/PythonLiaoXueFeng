a = [1, 2, 3, 4]
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(a.__iter__())
# print(a.__iter__())

# 下面两个for循环的返回值是相同的，可以证明for循环即调用了__iter__方法
# for n in a.__iter__():
#     print(n)
# for n in a:
#     print(n)

# lsith函数也可以执行一个迭代对象
# a1 = list(a.__iter__())
# print(a1)




# class Node:
#     def __init__(self, value):
#         self._value = value    # 定义内部数据成员
#         self._children = []
#
#     # overrides method in object 覆盖了对象中的方法，即重写了父对象中的方法，即实现了多态
#     # python3默认继承对象object
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)
#
# # Example
# if __name__ == '__main__':
#     root = Node(0)         # 对象的实例化
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#     # Outputs Node(1), Node(2)
#     # for循环使用了root对象的迭代方法，将对象的迭代方法的返回值赋值给了循环变量
#     # 即一个对象是可迭代对象，必有__iter__方法
#     # 一个对象可以执行print函数，必有__repr__方法
#     for ch in root:
#         print(ch)

# with语句中，f是open()的返回值
# with open('/etc/passwd') as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end='')


# def frange(start, stop, increment):
#     x = start
#     while x < stop:
#         yield x
#         x += increment
# a = frange(0, 3, 0.5)
# print(a)
# for n in a:
#     print(n)
