# -*- coding:utf-8 -*-
import unicodedata

__author__ = 'gjw'
__time__ = '2018/1/19 0019 上午 11:32'

# 4-6 如何去掉字符串中不需要的字符

"""
    方法一：字符串strip(),lstrip(),rstrip()方法去掉字符串两端的字符
"""
s = "     abc   123    "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print()
s = '---abc+++'
# 去掉包含的字符
print(s.strip('-+'))

print()
print()
"""
    方法二：删除单个固定位置的字符，可以使用切片+拼接的方式
"""
s = 'abc:123'
print(s[:3] + s[4:])


print()
print()
"""
    方法三：字符串的replce()方法或正则表达式re.sub()删除任意位置字符
"""
s = '\tabc\t123\txyz'
print(s.replace('\t', ''))

print()
import re
s = '\tabc\t123\txyz\ropq\r'
r = re.sub('[\t\r]', '', s)
print(r)

print()
print()
"""
    方法四：字符串translate()方法，可以同时删除多种不同字符
"""
import string
s = 'abc1230323xyz'
news = s.maketrans('abcxyz', 'xyzabc')
print(s.translate(news))

print()
s = 'abc\refg\n2342\t'
str_trans = str.maketrans('','','\r\n\t')
print(s.translate(str_trans))

# # 去掉汉语拼音音调
# u = 'èěéēàǎā'
# print('è'.encode())
# print(u)
# newu = u.translate(dict.fromkeys([0xc3,0xa8]))
# print(newu)