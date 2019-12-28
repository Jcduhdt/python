from chapter3.commodity_data_2 import sheet_qunar_zyx
import time

'''
Tool: pycharm
book: 爬虫、数据清洗与可视化实战
author: zhangxiong
date: 2019-12-27
备注：先运行commodity_data_2使其爬取数据存到数据库
然后运行该文件，读取数据库那张表，每隔10秒打印表中数据量
'''
while True:
    print(sheet_qunar_zyx.find().count())
    time.sleep(10)