from chapter3.commodity_data_3 import get_all_data
from chapter3.commodity_data_3 import dep_list
from multiprocessing import Pool  # 多进程爬虫用的库是Pool，可以自定义开启多进程数量，默认有几个CPU就开几个进程

'''
Tool: pycharm
book: 爬虫、数据清洗与可视化实战
author: zhangxiong
date: 2019-12-28
多线程启动commodity_data_3
'''

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_data, dep_list.split())  # 使用pool.map()将第二个参数映射到第一个参数（函数）上
