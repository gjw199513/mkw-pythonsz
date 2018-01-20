# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 下午 3:44'

# 7-6 如何使用描述符对实例属性做类型检查

"""
    在某项目中，我们实现了一些类，并希望能像静态类型语言
    那样(C, C++, Java)对它们的实例属性做类型检查。
    p = Person()
    p.name = 'Bob' # 必须是str
    p.age = 18     # 必须是int
    p.height = 1.83 # 必须是float
    
    要求：
    1.可以对实例变量名指定类型
    2.赋予不正确类型时抛出异常
"""

"""
    使用描述符来实现需要类型检查的属性：
    分别实现__get__,__set__,__delete__方法，
    在__set__内使用isinstance函数做类型检查
"""

"""
    原理：需要重新理解
"""


class Descriptor(object):
    def __get__(self, instance, cls):
        print('in __get__',instance, cls)
        return instance.__dict__['x']

    def __set__(selfs, instance, value):
        print('in __set__')
        instance.__dict__['x']=value

    def __delete__(self, instance):
        print('in __del__')


class A(object):
    x = Descriptor()


a = A()
a.x = 5
print(a.x)

# 实现


class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('需要一个 %s' % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    heigth = Attr('height', float)


p = Person()
p.name = 'Bob'
print(p.name)
p.age = '17'
