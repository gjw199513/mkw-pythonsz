# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 3:44'

# 5-3 如何设置文件的缓冲
"""
    全缓冲：open函数的buffering设置为大于1的整数n，n为缓冲区大小
"""
f = open('demo.txt', 'w', buffering=2048)
f.write('abc')

"""
    行缓冲：open函数的buffering设置为1
"""
f = open('demo.txt', 'w', buffering=1)

"""
    无缓冲：open函数的buffering设置为0 
"""
f = open('demo.txt', 'w', buffering=0)