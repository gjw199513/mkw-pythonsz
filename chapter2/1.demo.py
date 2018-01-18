# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 上午 10:13'

# 2-1 如何在列表, 字典, 集合中根据条件筛选数据

from random import randint

"""
    实现筛选大于零的数字
"""
# 随机生成范围在-10到10的十个数
data = [randint(-10, 10) for _ in range(10)]
print(data)

# 使用filter和lambda实现筛选大于零的数字
a = filter(lambda x: x >= 0, data)
print([x for x in a])


# 使用列表解析实现筛选大于零的数字
print([x for x in data if x >= 0])
# 首选列表解析


print()
print()
"""
    筛出字典值大于90的项
"""
# 随机生成20个学生的成绩
d = {x: randint(60, 100) for x in range(1, 20)}
print(d)
# 筛选出大于90的学生
print({k: v for k, v in d.items() if v > 90})


"""
    筛出集合能被3整除的元素
"""
s = set(data)
print({x for x in s if x % 3 == 0})
