#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 一个实例(instance)既可以是既可以是子类类型，也可以是父类类型

# 类名需要大写
# python3默认继承object对象
class Animal(object):
    def run(self):
        print('Animal is running...')

# 继承Animal对象
class Dog(Animal):
    # 发放重写
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

# python最大的一个特点是不需要指定变量的类型
# 变量名只是命名空间的一个符号，可以随时指向任何数据类型
# 此处的animal只是一个符号而已，从后面的animal.run()可以看出这是一个类
# 此处的多态表示为，只要传入的变量有.run方法，函数便可以运行
def run_twice(animal):
    animal.run()

a = Animal()
b = 5
d = Dog()
c = Cat()


print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(a)
# 'int' object has no attribute 'run'
# run_twice(b)
run_twice(d)
run_twice(c)