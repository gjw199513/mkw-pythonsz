# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 上午 10:44'

# 6-5 如何读写excel文件
"""
    利用pip安装：pip install xlrd,xlwt
    使用第三方库xlrd和xlwt，这两个库分别用于excel读和写
"""
import xlrd
# 读取excel
book = xlrd.open_workbook('demo5.xlsx')
# 访问文件中所有的表
book.sheets()
# 访问文件中指定索引的表
sheet = book.sheet_by_index(0)
# 访问行数
print(sheet.nrows)
# 访问列数
print(sheet.ncols)
# 访问指定单元格
print(sheet.cell(0, 0))
cell = sheet.cell(0, 0)
# 内容类型,通过xlrd.XL~来查看数字所对应的类型
print(cell.ctype)
# 访问值
print(cell.value)
"""
    下述行方法同样适用于列：col
"""
# 访问一行
print(sheet.row(1))
# 获取一行的值
print(sheet.row_values(1))
# 可以指定切片操作
print(sheet.row_values(1, 1))
# 添加单元格
sheet.put_cell()

print()
print()
# 写入excel
import xlwt
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('sheet1')
# 写入文件
wsheet.write()