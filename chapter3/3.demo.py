# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 下午 4:11'

# 3-3 如何使用生成器函数实现可迭代对象

# 实现一个可迭代对象的类，它能迭代出给范围内所有素数


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False

        for i in range(2, k):
            if k % i == 0:
                return False
            return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k


for x in PrimeNumbers(1, 100):
    print(x)