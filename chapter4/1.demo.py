# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 上午 9:37'

# 4-1 如何拆分含有多种分隔符的字符串

"""
    方法一：连续使用是str.split()方法，每次处理一种分隔符
"""


def mySplit(s, ds):
    # 将字符串放入列表之中
    res = [s]

    for d in ds:
        t = []
        """
            map函数匹配同类型分隔符，并将其分割
            通过遍历ds可以将所有分隔符遍历
        """
        [t.extend(x) for x in map(lambda x: x.split(d), res)]
        res = t
    # 过滤掉空字符串
    return [x for x in res if x]


s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
print(mySplit(s, ';,|\t'))


"""
    方法二：使用正则表达式的re.split()方法，一次性拆分字符串
    推荐!!!!!!!!!!
"""
import re
r = re.split(r'[,;\t|]+',s)
print(r)

"""
    对于单一分隔符使用字符串自带的split
    对于多种分隔符使用re模块中的split
"""