# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 4:00'

# 5-5 如何访问文件的状态
"""
    系统调用：标准库中os模块下的三个系统调用stat，fstat，lstat获取文件状态
"""
import os
import stat
import time
s = os.stat('py3.txt')
# 判断是否是文件夹
print(stat.S_ISDIR(s.st_mode))
# 判断常规文件
print(stat.S_ISREG(s.st_mode))
# 判断读权限，返回非0值则可以读
print(s.st_mode & stat.S_IRUSR)
# 判断执行权限，返回非0值则可以读
print(s.st_mode & stat.S_IXUSR)
# 文件的最后访问时间
print(time.localtime(s.st_atime))
# 普通文件的大小
print(s.st_size)


print()
print()
"""
    快捷函数：标准库中os.path下一些函数，使用起来更加简洁
"""
# 判断是否是目录
print(os.path.isdir('py3.txt'))
# 判断是否是符号链接
print(os.path.islink('py3.txt'))
# 判断是否是普通文件
print(os.path.isfile('py3.txt'))
# 显示文件访问时间
print(os.path.getatime('py3.txt'))
# 显示文件大小
print(os.path.getsize('py3.txt'))