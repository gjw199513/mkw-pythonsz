# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/2/19 12:06'

# 9-4 如何实现属性可修改的函数装饰器

# 为分析程序内哪些函数执行时间开销较大，我们定义一个带
# timeout参数的函数装饰器。装饰功能如下：

# 1.统计被装饰函数单次调用运行时间。
# 2.时间大于参数timeout的，将此次函数调用记录到log日志中。
# 3.运行时可修改timeout的值


"""
    为包裹函数增添一个函数，用例修改闭包中使用的自由变量。
    在python3中：使用nonlocal访问嵌套作用域中的变量引用
"""
from functools import wraps
import time
import logging


def warn(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            used = time.time() - start
            if used > timeout:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout)
                logging.warn(msg)
            return res

        def setTimeout(k):
            nonlocal timeout
            timeout = k

        wrapper.setTimeout = setTimeout
        return wrapper

    return decorator


from random import randint


@warn(1.5)
def test():
    print('In text')
    while randint(0, 1):
        time.sleep(0.5)


for _ in range(30):
    test()
test.setTimeout(1)
for _ in range(30):
    test()
