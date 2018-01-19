# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 上午 10:27'

# 4-3 如何调整字符串中文本的格式

"""
    使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，
    捕获每个部分内容，在替换字符串中调整各个捕获组的顺序
"""
# 将2016-05-23转换为05/28/2016
# 用字符串模拟log文件
s = """
    2016-05-23 10.29:28 ASDASD ASLDKJ-ada aslkdj-asdjl ahsdlj-adlkjasd 21.2321asdj
    2016-05-23 10.29:28 ASDASghjghD ASLDKdffgfgJ-ada aslkdj-asdjl ahsdlj-adlkjfhhfasd 21.2321asdj
    2016-05-23 10.29:28 hjhjkhjghDASD ASLDKJ-ada aslkdj-asdjl gfhfh-adlkjasd 21.2321asdj
    2016-05-23 10.29:28 ASDAghjghjfhjghSD ASLDKJ-ada aslfghfghkdj-asdjl ahsdlj-gfdggf 21.2321asdj
    2016-05-23 10.29:28 AdgfdfgSDASD ASLDKJ-ada aslkdj-asdjl ahsdlj-adlkjasd 21.2321asdj
"""
import re
"""
    每组用括号表示，通过数字来读取组（从1开始，并且在组号前加入\）
"""
r1 = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s)
print(r1)

print()
print()

"""
    通过?P<name>来给每组命名，然后使用g<name>来读取名字
    从而实现为捕获组命名，用名字来修改各组的效果，不需要使用数字
"""
r2 = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', s)
print(r2)
