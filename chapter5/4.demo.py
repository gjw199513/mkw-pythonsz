# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 3:53'

# 5-4 如何将文件映射到内存

"""
    使用标准库中mmap模块的mmap()函数,它需要一个打开的文件描述符作为参数。
"""
import mmap

f = open("demo.bin", 'r+b')
f.fileno()
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

type(m)
print(m[0])
m[0] = '\x88'
m[4:8] = '\xff' * 4
