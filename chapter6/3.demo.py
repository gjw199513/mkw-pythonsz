# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 上午 9:27'

# 6-3 如何解析简单的xml文档

"""
    使用标准库中的xml.etree.ElementTree,其中的parse函数可以解析xml文档
"""

from xml.etree.ElementTree import parse
f = open('demo3.xml')

et = parse(f)
# 根节点
root = et.getroot()
print(root)
# 该节点的标签
print(root.tag)
# 该节点的属性
print(root.attrib)
# 该节点的文本内容
print(root.text)

print()

# 获取给节点的子节点
# 该方法可能会被删除
print(root.getchildren())

for child in root:
    print(child.get('name'))


print()
# 找到root节点的下一层节点，只显示第一个出现
print(root.find('PLANT'))
# 找到root节点的下一层的所有节点
print(root.findall('PLANT'))
# 将找到节点变成可迭代对象
print(root.iterfind('PLANT'))
print("---")
for e in root.iterfind('PLANT'):
    print(e.tag)

# 找到root下的所有节点
print(list(root.iter()))
# 传入参数可以寻找指定的节点
print(list(root.iter("ZONE")))

print("----------")
# *找到所有，前面可以加限制条件
print(root.findall('PLANT/*'))
# .寻找当前的
print(root.findall('.'))
# //找到任意层级下的
print(root.findall('.//ZONE'))
# ..找到父对象
print(root.findall('.//ZONE/..'))
# 找到包含属性的
print(root.findall('PLANT/COMMON[@name]'))
# 找到属性包含特定值的
print(root.findall('PLANT/COMMON[@name="b"]'))
# 找到指定元素必须包含子元素
print(root.findall('PLANT[C]'))
# 找到指定元素必须包含子元素对应的值
print(root.findall('PLANT[C="CCC"]'))
# 找到指定元素的对应位置
print(root.findall('PLANT[1]'))
# 找到最后一个
print(root.findall('PLANT[last()]'))