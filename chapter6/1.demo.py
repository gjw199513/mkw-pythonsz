# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 4:34'

# 6-1 如何读写csv数据
from urllib.request import urlretrieve

# 下载文件到pingan.csv中，由于链接失效，所以用本地文件
# urlretrieve('http://finance.yahoo.com/d/quotes.csv?s=000001.sz', 'pingan.csv')

import csv
rf = open('pingan.csv', 'r')
# 读取
readers = csv.reader(rf)
for row in readers: print(row)

# 写入
rf.seek(0)
wf = open("pingan_copy.csv", 'w')
writers = csv.writer(wf)
writers.writerow(readers.__next__())
