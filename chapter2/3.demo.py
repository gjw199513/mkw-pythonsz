# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 上午 10:51'

# 2-3 如何统计序列中元素的出现频度

from random import randint
# 找到数字中出现次数最高的3个元素，它们出现了多少次
"""
    使用列表解析+字典排序实现
"""
data = [randint(0, 20) for _ in range(30)]
print(data)
# 将出现次数进行统计
c = dict.fromkeys(data, 0)
for x in data:
    c[x] += 1
print(c)

# 将生成的统计字典进行排序排序
c = sorted(c.items(), key=lambda x: x[1], reverse=True)[:3]
d = dict(c)
print(d)

"""
    使用counter完成
"""
from collections import Counter
c2 = Counter(data)
print(c2.most_common(3))


# 对文件（CodingStyle.txt）中的词频进行统计
"""
    使用counter完成
"""
import re
txt = open("CodingStyle.txt").read()
c3 = Counter(re.split('\W+', txt))
print(c3.most_common(10))