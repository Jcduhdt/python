import requests
import json

'''
@Time 2020-1-2
@author zhangxiong
@software pycharm
爬取六间房全站短视频

思路：
1.确定爬取url路径，headers参数
2.发送请求 --requests模拟浏览器发送请求，获取响应数据
3.解析数据 --json 把json字符串转化为python可交互的数据类型
4.保存数据 -- 保存在目标文件夹中
'''


def video_spider():
    for page in range(10):
        print('----------------------正在抓取第{}页数据----------------------------'.format(page+1))
        # 1.确定爬取url路径，headers参数
        base_url = 'https://v.6.cn/minivideo/getlist.php'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/79.0.3945.88 Safari/537.36'
        }
        params = {
            'act': 'recommend',
            'page': str(page + 1),
            'pagesize': '20'
        }
        # 2.发送请求 --requests模拟浏览器发送请求，获取响应数据
        response = requests.get(url=base_url, headers=headers, params=params)
        data = response.text  # 得到的是response的json模块

        # 3.解析数据 --json 把json字符串转化为python可交互的数据类型
        # 3.1转换数据类型
        dict_data = json.loads(data)  # 将json转换成字典
        # 3.2解析数据
        dict_list = dict_data['content']['list']  # 列表

        # 遍历列表下的字典
        for video_list in dict_list:
            video_title = video_list['title'] + '.mp4'  # 视频的标题
            video_url = video_list['playurl']  # 视频的链接
            print('正在下载：', video_title)
            video_data = requests.get(video_url, headers=headers).content  # 因为返回的是response 要写进文件久要转成二进制

            # 4.保存数据 -- 保存在目标文件夹中
            with open('E:/video/' + video_title, 'wb') as f:
                f.write(video_data)
    print('下载完毕')


if __name__ == "__main__":
    video_spider()
