# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 上午 10:39'

# 2-2 如何为元组中的每个元素命名, 提高程序可读性

"""
    使用类似枚举的常量进行定义，常量一般为大写
"""
NAME, AGE, SEX, EMAIL = range(4)
student = ('Jim', 16, 'male', 'jim8721@gmail.com')

#NAME
print(student[NAME])

#AGE
if student[AGE] >= 18:
    pass
#SEX
if student[SEX] == 'male':
    pass


"""
    使用namedtuple代替tuple
"""
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('Jim', 16, 'male', 'jim8721@gmail.com')
print(s)
