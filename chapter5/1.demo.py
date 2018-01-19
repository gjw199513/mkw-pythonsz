# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 2:35'

# 5-1 如何读写文本文件
f = open("py3.txt", "wt", encoding="utf8")
f.write("你好，我的世界")
f.close()
f = open("py3.txt", "rt", encoding="utf8")
s = f.read()
print(s)