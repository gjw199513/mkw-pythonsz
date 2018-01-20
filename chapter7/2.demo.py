# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 下午 2:10'

# 7-2 如何为创建大量实例节省内存
"""
    某网络游戏中，定义了玩家类Player(id,name,status,...)
    每有一个在线玩家，在服务器程序内则有一个Player的实例，
    当在线人数很多时，将产生大量实例。(如百万级）
    
    如何降低这些大量实例的内存开销？
"""

"""
    解决方案：定义类的__slots__属性，它是用来声明实例属性名字的列表
"""


class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2(object):
    """'
        提前声明属性，不能进行动态绑定
    """
    __slots__ = ['uid', 'name', 'stat', 'level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


p1 = Player('0001', 'Jim')
p2 = Player2('0001', 'Jim')
"""
    对于两个实例大小有差距，必然是二者属性不同
    使用集合找出二者的差集
"""
print(set(dir(p1)) - set(dir(p2)))
print(p1.__dict__)