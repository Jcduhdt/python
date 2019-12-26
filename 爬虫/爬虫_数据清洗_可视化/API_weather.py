import requests
import time
import pymongo
'''
Tool: pycharm
book: 爬虫、数据清洗与可视化实战
author: zhangxiong
date: 2019-12-26
使用mongoDB
要先在cmd开启mongoDB，在右边建立mongo的链接,再运行此文件，可看到数据
'''
# 建立连接
client = pymongo.MongoClient('localhost', 27017)
# 在MongoDB中新建名为weather的数据库
book_weather = client['weather']
# 在weather库中新建名为sheet_weather_3的表
sheet_weather = book_weather['sheet_weather_3']
url = 'https://cdn.heweather.com/china-city-list.txt'
html = requests.get(url)
html.encoding = 'utf-8'
data = html.text
data1 = data.split("\n")  # 将文本转成列表  书上是\r不行，但是现在好像是\n分段
# print(data1)
for i in range(6):  # 通过一个循环将前三行无用的删除
    data1.remove(data1[0])
for item in data1[0:10]:  # 提取城市/地区编码,城市太多了就提取了前10个
    print(item[1:13])
    url = 'https://free-api.heweather.net/s6/weather/forecast?location=' \
          + item[1:13] + '&key=8586ba40bce549ffa0f5d6370805722f'
    html = requests.get(url)
    html.encoding = 'utf-8'
    time.sleep(1)
    dic = html.json()  # 这个会覆盖
    # 向表写入一条数据
    sheet_weather.insert_one(dic)
# 查找键 HeWeather6.basic.location 值为北京的数据
for item in sheet_weather.find({'HeWeather6.basic.location': '北京'}):
    print(item)
# 查找键 HeWeather6.basic.location 值为北京的数据
for item in sheet_weather.find():
    # 因为数据需要3天的天气预报，因此循环3次
    for i in range(3):
        tmp = item['HeWeather6'][0]['daily_forecast'][i]['tmp_min']
        # 使用update方法，将表中最低温数据修改为数值型
        sheet_weather.update_one({'_id': item['_id']},  # 要跟新的查询条件
                                 {'$set': {'HeWeather6.0.daily_forecast.{}.tmp_min'.format(i): int(tmp)}})  # 要跟新的信息
        # $set是MongoDB的修改器，用于指定一个键并更新键值，若键不存在则创建一个键
        # 其他修改如$inc数字型的键进行增减 $unset删除键 $push向文档某数组类型的键添加一个数组元素
        # 提取出最低气温低于5摄氏度的城市
        # $gt表示符号> $lt表示< $lte表示<= $gte表示=>
for item in sheet_weather.find({'HeWeather6.daily_forecast.tmp_min': {'$gt': -6}}):  # 找到温度大于-6度的城市
    print(item['HeWeather6'][0]['basic']['location'])
