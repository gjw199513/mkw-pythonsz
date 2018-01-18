# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 下午 4:32'

# 3-4 如何进行反向迭代以及如何实现反向迭代

l = [1, 2, 3, 4, 5]
"""
    使用reverse方法实现改变原来的列表
    使用反向切片浪费空间
    
    使用revered内置函数较为合适
"""
for x in reversed(l):
    print(x)

print()
print()


class FloatRange:
    def __init__(self, start, end, step=0.1):
       self.start = start
       self.end = end
       self.step = step

    # 正向迭代
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    # 反向迭代
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for x in FloatRange(1.0, 4.0, 0.5):
    print(x)

print()
print()

for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x)