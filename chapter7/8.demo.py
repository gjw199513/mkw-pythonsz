# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 下午 4:25'

# 7-8 如何通过实例方法名字的字符串调用方法

"""
    某项目中，我们的代码使用了三个不同库中的图形类：
        Circle,Triangle,Rectangle
        
    他们都有一个获取图形面积的接口(方法),但接口名字不同。
    我们可以实现一个统一的获取面积的函数，使用每种方法名
    进行尝试，调用相应类的接口。
"""


class Circle(object):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14


class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        a, b, c = self.a, self.b, self.c
        # 海伦面积公式
        p = (a + b + c) / 2
        area = (p*(p-a)*(p-b)*(p-c))**0.5
        return area


"""
    方法一:使用内置函数getattr,通过名字在实例上获取方法对象，然后调用。
"""


def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name, None)
        if f:
            return f()


shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)

shapes = [shape1, shape2, shape3]
print([x for x in map(getArea, shapes)])

"""
    方法二：使用标准库operator下的methodcaller函数调用
"""
from operator import methodcaller
s = 'abc123abc456'
print(s.find('abc', 4))
# 和上的find实现类似功能，为了演示methodcaller函数
print(methodcaller('find', 'abc', 4)(s))

print("----")
# 实现方法一的操作
"""
    methodcaller实现函数的调用，
    第一个参数是函数名，后面是函数的参数
    函数后加入调用的实例即可完成调用
"""
print(methodcaller('area')(shape1))
print(methodcaller('getArea')(shape2))
print(methodcaller('get_area')(shape3))