import requests
import urllib
import time
import pymongo

'''
Tool: pycharm
book: 爬虫、数据清洗与可视化实战
author: zhangxiong
date: 2019-12-27
使用mongoDB
要先在cmd开启mongoDB，在右边建立mongo的链接,再运行此文件，可看到数据
爬取旅游的数据存入mongoDB，不过后面会无法获取数据，可能是爬快了，也许是网站是动态加载的原因
对commodity_data的代码优化
'''

client = pymongo.MongoClient('localhost', 27017)  # 获取mongoDB的连接
book_qunar = client['qunar']  # 建库
sheet_qunar_zyx = book_qunar['qunar_zyx']  # 建表


def get_list(dep, item):
    url = 'https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail' \
          '&dep={}&query={}&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C' \
          '&cfrom=zyx&it=dujia_hy_destination&date=&needNoResult=true&originalquery={}' \
          '&limit=0,28&includeAD=true&qsact=search' \
        .format(urllib.request.quote(dep), urllib.request.quote(item), urllib.request.quote(item))
    html = get_json(url)
    routeCount = int(html['data']['limit']['routeCount'])  # 起始地到目的地的产品数
    for limit in range(0, routeCount, 20):  # 以routeCount为迭代次数的终点
        url = 'https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail&dep={}&query={}' \
              '&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx' \
              '&it=dujia_hy_destination&date=&needNoResult=true&originalquery={}&limit={},28&includeAD=true' \
              '&qsact=search'.format(urllib.request.quote(dep), urllib.request.quote(item),
                                     urllib.request.quote(item), limit)
        html = get_json(url)
        result = {
            'data': time.strftime('%Y-%m-%d', time.localtime(time.time())),  # 存入运行此程序的年月日
            'dep': dep,  # 起始地
            'arrive': item,  # 目的地
            'limit': limit,  # 次数？
            'result': html # 查找结果
        }
        sheet_qunar_zyx.insert_one(result)


def get_json(url):
    html = requests.get(url)
    time.sleep(1)
    return html.json()


if __name__ == '__main__':
    url = 'https://touch.dujia.qunar.com/depCities.qunar'
    dep_dict = get_json(url)
    for dep_item in dep_dict['data']:
        for dep in dep_dict['data'][dep_item]:  # dep即起始地
            a = []
            url = 'https://touch.dujia.qunar.com/golfz/sight/arriveRecommend?dep={}' \
                  '&exclude=&extensionImg=255,175'.format(urllib.request.quote(dep))
            arrive_dict = get_json(url)
            for arr_item in arrive_dict['data']:
                for arr_item_1 in arr_item['subModules']:
                    for query in arr_item_1['items']:
                        if query['query'] not in a:  # 对目的地去重
                            a.append(query['query'])
            for item in a:
                get_list(dep, item)
