# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 上午 10:09'

# 6-4 如何构建xml文档
"""
    使用标准库中的xml.etree.ElementTree,构建ElementTree,使用write方法写入文件
"""
from xml.etree.ElementTree import Element, ElementTree, tostring
# 传入一个tag
e = Element('Data')
print(e.tag)
e.set('name', 'abc')
# 将原文件转为xml格式字符串
print(tostring(e))
# 设置文本内容
e.text = '123'
print(tostring(e))
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
# 增加子元素
e2.append(e3)
print(tostring(e2))
e.text = None
e.append(e2)
print(tostring(e))

et = ElementTree(e)
et.write('demo4.xml')