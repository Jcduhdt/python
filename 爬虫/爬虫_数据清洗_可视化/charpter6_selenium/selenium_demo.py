import requests
import urllib
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By  # By库用于指定HTML文件中DOM标签元素
from selenium.webdriver.support.ui import WebDriverWait  # 用于等待网页加载完成
from selenium.webdriver.support import expected_conditions as EC  # 用于指定等待网页加载结束的条件


def get_url(url):
    time.sleep(5)
    return requests.get(url)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    dep_cities = ["北京", "上海", "广州", "深圳", "天津", "杭州", "南京", "济南", "重庆", "青岛", "大连", "宁波", "厦门",
                  "成都", "武汉", "哈尔滨", "沈阳", "西安", "长春", "长沙", "福州", "郑州", "石家庄", "苏州", "佛山", "烟台",
                  "合肥", "昆明", "唐山", "乌鲁木齐", "兰州", "呼和浩特", "南通", "潍坊", "绍兴", "邯郸", "东营", "嘉兴",
                  "泰州", "江阴", "金华", "鞍山", "襄阳", "南阳", "岳阳", "漳州", "淮安", "湛江", "柳州", "绵阳"]
    for dep in dep_cities:
        html = get_url('https://touch.dujia.qunar.com/golfz/sight/arriveRecommend?dep=' + urllib.request.quote(dep) + \
                       '&exclude=&extensionImg=255,175')
        arrive_dict = html.json()
        for arr_item in arrive_dict['data']:
            for arr_item_1 in arr_item['subModules']:
                for query in arr_item_1['items']:
                    driver.get("https://fh.dujia.qunar.com/?tf=package")
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "depCity")))
                    # EC.presence_of_element_located用于指定标志等待结束的DOM元素，(By.ID, "depCity")指定id='depCity'
                    driver.find_element_by_xpath("//*[@id='depCity']").clear()  # 清除输入框的数据
                    driver.find_element_by_xpath("//*[@id='depCity']").send_keys(dep)  # 填入出发地
                    driver.find_element_by_xpath("//*[@id='arrCity']").send_keys(query["query"])  # 填入目的地
                    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/a").click()  # 点击开始指定按钮
                    print("dep:%s arr:%s" % (dep, query["query"]))
                    for i in range(100):
                        time.sleep(random.uniform(5, 6))
                        # 定位到搜索结果页的页码按钮，若定位不到则表示结果为空，跳出循环
                        pageBtns = driver.find_elements_by_xpath("html/body/div[2]/div[2]/div[8]")
                        if pageBtns == []:
                            break
                        routes = driver.find_elements_by_xpath("html/body/div[2]/div[2]/div[7]/div[2]/div")
                        for route in routes:  # 找到对应数据，然后分块取出数据
                            result = {
                                'date': time.strftime('%Y-%m-%d', time.locatime(time.time())),
                                'dep': dep,
                                'arrive': query['query'],
                                'result': route.text
                            }
                        if i < 9:  # 指定页码和翻页，设定10页，检测不到下一页元素就跳出循环
                            btns = driver.find_elements_by_xpath("html/body/div[2]/div[2]/div[8]/div/div/a")
                            for a in btns:
                                if a.text == u"下一页":
                                    a.click()
                                    break
    driver.close()
