# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 2:44'

# 5-2 如何处理二进制文件
f = open("背景.wav", "rb")
info = f.read(44)
print(info)

import struct
print(struct.unpack('h', info[22:24]))
print(struct.unpack('i', info[24:28]))
print(struct.unpack('h', info[34:36]))

import array
import math
f.seek(0, 2)
f.tell()
n = math.ceil((f.tell() - 44) / 2)
buf = array.array('h', (0 for _ in range(n)))
f.seek(44)
f.readinto(buf)

for i in range(n):
    buf[i] /= 8.0
f2 = open('demo.wav', 'wb')
f2.write(info)
buf.tofile(f2)
f2.close()