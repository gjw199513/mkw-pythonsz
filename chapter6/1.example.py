# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/19 0019 下午 4:51'

# 案例读写脚本
import csv

with open('pingan.csv', 'r') as rf:
    reader = csv.reader(rf)
    with open('pingan2.csv', 'w') as wf:
        writer = csv.writer(wf)
        headers = reader.__next__()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)

print("end")
