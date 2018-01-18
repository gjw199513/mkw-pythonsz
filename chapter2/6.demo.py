# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 下午 2:21'

# 2-6 如何让字典保持有序
"""
    使用OrderedDict实现,原有字典没有记录顺序
"""
from collections import OrderedDict
d = OrderedDict()
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)
for k in d: print(k)
print()
print()
print()


# 模拟竞赛系统
from time import time
from random import randint
from collections import OrderedDict
# 生成用户
players = list('ABCDEFGH')
# 创建成绩表
d = OrderedDict()
l = len(players)
# 竞赛开始
start = time()
for i in range(l):
    # 选手答题
    input()
    # 答完题的选手离场
    p = players.pop(randint(0, l - 1 - i))
    end = time()
    print(i+1, p, end-start)
    d[p] = (i + 1, end-start)

print('-'*20)
for k in d:
    print(k, d[k])