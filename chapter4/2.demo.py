# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 上午 10:06'

# 4-2 如何判断字符串a是否以字符串b开头或结尾

"""
    使用字符串的str.startswith()和str.endswith()方法。
    注意：多个匹配时参数使用元组。
"""
# 在当前目录中找到.sh和.py结尾的文件
import os, stat
# 该目录下的文件用列表代替
f = ['e.py', 'g.sh', 'd.java', 'h.c', 'f.cpp', 'a.sh', 'c.h', 'b.py']
r = [name for name in f if name.endswith(('.sh', '.py'))]
print(r)

# 修改文件的权限,为用户增加可执行权限（Linux下的操作）
# 读取需要修改的文件，找出st_mode（权限码）对其修改
m = os.stat('e.py').st_mode
# 将权限码转换为八进制
m = oct(m)
# 用户执行权限码
u = oct(stat.S_IXUSR)
os.chmod('e.py', m | u)