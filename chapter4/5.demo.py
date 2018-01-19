# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 上午 11:19'

# 4-5 如何对字符串进行左, 右, 居中对齐

"""
    方法一：使用字符串的str.ljust(),str.rjust(),str.center()进行左，右，居中对齐
"""
s = "abc"
l = s.ljust(20)
print(l)
r = s.rjust(20)
print(r)
c = s.center(20)
print(c)


print()
print()
"""
    使用format()方法，传递类似'<20','>20','^20'参数完成同样的任务
"""
print(format(s, '<20'))
print(format(s, '>20'))
print(format(s, '^20'))


# 将字典中的文字对齐
print()
print()
d = {"DistCull": 500.0,
     "SmallCull": 0.04,
     "farclip": 477,
     "lodDist": 100.0,
     "trilinear": 40}

w = max([x for x in map(len, d.keys())])
for k in d:
    print(k.ljust(w), ':', d[k])