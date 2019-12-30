from scrapy.cmdline import execute
'''
有问题，股市的html界面展现已经不同于作者当时的页面
所以字段什么的都需要更改
而且那个page获取那里总是提示问题，又不太懂这个框架，所以还没调出来
'''
execute(["scrapy", "crawl", "stock", "-o", "items.json"])
# 等价于在cmd环境该项目路径下执行"scrapy crawl stock -o items.json"
# 将爬取的数据导出到items.json文件
