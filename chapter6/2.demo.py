# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 5:13'

# 6-2 如何读写json数据
"""
    使用标准库中的json模块，其中loads，dumps函数可以完成json数据的读写
"""
import json
l = [1, 2, 'abc', {'name': 'Bpb', 'age': 13}]
"""
    dumps将python对象转换为json字符串
"""
print(json.dumps(l))
d = {'b': None, 'a': 5, 'c': 'abc'}
print(json.dumps(d))

"""
    去掉分隔符的空格
"""
print(json.dumps(l, separators=[',', ':']))

"""
    对输出的字典排序
"""
print(json.dumps(d, sort_keys=True))

print()
l2 = json.loads('[1, 2, "abc", {"name": "Bob", "age": 13}]')
print(l2)

"""
    dump实现的文件接口
    将Json文件转为字典
"""
with open("demo.json", 'w') as f:
    json.dump(l, f)
