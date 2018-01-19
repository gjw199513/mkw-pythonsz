# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 4:19'

# 5-6 如何使用临时文件

"""
    使用标准库中tempfile下的TemporaryFile，NamedTemporaryFile
"""
from tempfile import TemporaryFile, NamedTemporaryFile
# TemporaryFile文件系统路径无法找到
f = TemporaryFile()
f.write(('abcdef' * 100000).encode())
f.seek(0)
print(f.read(100))

# NamedTemporaryFile可以找到，多个进程可以访问
ntf = NamedTemporaryFile()
print(ntf.name)

"""
    delete=False可以不删除临时文件
"""
ntf1 = NamedTemporaryFile(delete=False)
