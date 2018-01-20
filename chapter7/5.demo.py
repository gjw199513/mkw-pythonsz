# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 下午 3:24'

# 7-5 如何让类支持比较操作
"""
    有时我们希望自定义的类，实例间可以使用<,<=,>,>=,==,!=
    符号进行比较，我们自定义比较的行为，例如，有一个矩形的类，
    我们希望比较两个矩形的实例时，比较的是他们的面积
    class Rectangle:
        def __init__(self, w, h):
            self.w = w
            self.h =h
            
        def area(self):
            return self.w*self.h
            
    rect1 = Rectangle(5,3)
    rect2 = Rectangle(4,4)
    rect1 > rect2 # => rect.area() > rect2.area()
"""

"""
    比较符号运算符重载，需要实现以下方法：
    __lt__,__le__,__gt__,__ge__,__eq__,__ne__
    使用标准库下的functools下的类装饰器total_ordering可以简化此过程
"""


class Rectangle1(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    # 小于
    def __lt__(self, obj):
        return self.area() < obj.area()

    # 小于等于
    def __le__(self, obj):
        return self.area() <= obj.area()


r1 = Rectangle1(5, 3)
r2 = Rectangle1(4, 4)

print(r1 < r2)
print(r1 <= r2)


print()
print()


"""
  定义比较的抽象基类  
"""

from abc import ABCMeta, abstractmethod


"""
    使用标准库下的functools下的类装饰器total_ordering可以简化此过程
"""
from functools import total_ordering


@total_ordering
class Shape(object):

    # 抽象接口
    @abstractmethod
    def area(self):
        pass

    def __lt__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() < obj.area()

    # 小于等于
    def __eq__(self, obj):
        return self.area() == obj.area()


@total_ordering
class Rectangle2(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    # 装饰器使用方法：定义等于和其他中的一个
    # 小于
    def __lt__(self, obj):
        return self.area() < obj.area()

    # 小于等于
    def __eq__(self, obj):
        return self.area() == obj.area()


r1 = Rectangle2(5, 3)
r2 = Rectangle2(4, 4)

print(r1 < r2)
print(r1 <= r2)

