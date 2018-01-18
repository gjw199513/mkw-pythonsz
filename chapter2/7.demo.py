# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/18 0018 下午 2:38'

# 2-7 如何实现用户的历史记录功能(最多n条)
"""
    使用deque来保存有限制数的记录
"""
from collections import deque
from random import randint
import pickle
N = randint(0, 100)
# 存入五条历史记录
history = deque([], 5)


def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print(str(k) + " is less-than N")
    else:
        print(str(k) + " is greater-than N")
    return False


while True:
    line = input("please input a number:")
    """
        isdigit() 方法检测字符串是否只由数字组成。
    """
    if line.isdigit():
        k = int(line)
        history.append(k)
        # 通过if来判断函数执行结果
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(list(history))
"""
    必须以二进制（b）写入和读取
"""
# 将历史记录存储在文件中
s = pickle.dump(str(history), open('history.txt', 'ab'))
# 读取文件记录
q = pickle.load(open('history.txt', 'rb'))
print(q)