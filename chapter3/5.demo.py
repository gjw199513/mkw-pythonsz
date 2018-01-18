# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 下午 4:49'

# 3-5 如何对迭代器做切片操作
f = open("CodingStyle.txt")

# 读取文件中的每行
# 当文件过大，一次性读取会有问题
lines = f.readlines()
print(lines)

"""
    使用标准库中的itertools.islice,它能返回一个迭代对象切片的生成器
"""
from itertools import islice
f.seek(0)
"""
islice的参数：第一个是文件对象，后面的一个参数代表到n结尾
后面的两个参数代表起始到终止
"""
s = islice(f, 100, 300)
for line in s:
    print(line)
"""
    islice会消耗原来的迭代对象，需要重新创建
"""

