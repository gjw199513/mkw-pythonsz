# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 上午 11:29'

# 2-4 如何根据字典中值的大小, 对字典中的项排序
"""
    使用内置函数sorted
"""
from random import randint
"""
    使用zip函数转换为元祖，再进行排序
"""
# 产生随机的六个学生成绩
d = {x: randint(60,100) for x in 'xyzabc'}
s1 = sorted(zip(d.values(), d.keys()))
print(s1)

print()
print()

"""
    使用sorted函数的key参数
"""
s2 = sorted(d.items(), key=lambda x: x[1])
print(s2)