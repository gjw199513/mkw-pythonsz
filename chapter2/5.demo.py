# -*- coding:utf-8 -*-


__author__ = 'gjw'
__time__ = '2018/1/18 0018 上午 11:38'
# 2-5 如何快速找到多个字典中的公共键(key)

from random import randint, sample
# 选出每次都进球的球员
# 随机取样，从样本中选择n个
"""
    sample实现随机取样
"""
s1 = {x: randint(1, 4) for x in sample('abcefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcefg', randint(3, 6))}
print("{}\n{}\n{}".format(s1, s2, s3))

"""
    利用集合（set）的交集操作
"""

"""
    使用字典的keys()方法，得到一个字典keys的集合,然后进行交集操作
"""
print()
print()
print(s1.keys() & s2.keys() & s3.keys())

# 对于n轮，即n个集合
"""
    使用map函数，得到所有字典的keys的集合
    使用reduce函数，取所有字典的keys的集合的交集
"""
from functools import reduce

r = reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3]))
print(r)