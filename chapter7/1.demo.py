# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 上午 11:37'

# 7-1 如何派生内置不可变类型并修改实例化行为

"""
    我们想自定义一种新类型的元组，对于传入的可迭代对象，
    我们只保留作其中int类型且值大于0的元素，例如：
    IntTuple([1,-1,'abc',6,['x','y'],3])=>(1,6,3)
    
    要求IntTuple是内置tuple的子类，如何实现？
"""
"""
    解决方案：定义类IntTuple集成内置tuple，并实现__new__,修改实例化行为
"""


class IntTuple(tuple):
    """
        python3中不需要实现该方法
    """
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)
    # def __init__(self, iterable):
    #     # before
    #     super(IntTuple, self).__init__()
    #     # after


t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(t)