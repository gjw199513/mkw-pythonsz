# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 上午 10:24'

# 将csv文件转换为xml
import csv
from xml.etree.ElementTree import Element, ElementTree, tostring


def csvToXml(fname):
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        headers = reader.__next__()

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)

    return ElementTree(root)


et = csvToXml('pingan.csv')
et.write('pingan.xml')