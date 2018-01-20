# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/20 0020 上午 11:11'

# 实现excel的读写操作
import xlrd, xlwt

rbook = xlrd.open_workbook('demo5.xlsx')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
# 创建单元格
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)

for row in range(1, rsheet.nrows):
    # 将每行的值读取，出去第一列的姓名
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

wbook = xlwt.Workbook()
# 添加一张表
wsheet = wbook.add_sheet(rsheet.name)
# 对齐格式
style = xlwt.easyxf('align: vertical center, horizontal center')
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save("output.xls")