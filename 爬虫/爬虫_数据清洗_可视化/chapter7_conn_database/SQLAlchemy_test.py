# -*- coding:utf-8 -*-
# @Time : 2020/1/6 20:26
# @Author : Zhang
# @File : SQLAlchemy_test.py
# @Software: PyCharm
# 还要自己新建对应的库，表
# 感觉用起来还可以

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


# 定义Product对象
class Product(Base):
    def __init__(self, ID, name, type):
        self.ID = ID
        self.name = name
        self.class_name = type

    # 表的名字
    __tablename__ = 'Product'
    # 表的结构
    ID = Column(String(20), primary_key=True)
    name = Column(String(20))
    class_name = Column(String(20))


# 初始化数据库连接
# SQLAlchemy用一个字符串表示连接信息，'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名称'
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 向数据库添加一行记录
# 创建session对象
session = DBSession()
# 创建新Product对象
new_user = Product(ID='19558276', name='北京5天4晚自由行 含双早 入住前门商业街豪华酒店 含双人故宫电子门票', type='景+酒')
# 添加到session
session.add(new_user)
# 提交即保存到数据库
session.commit()

# DBSession对象可视为当前数据库连接
# 从数据库列表中查询数据
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
student = session.query(Product).filter(Product.ID == '19558276').one()
# 打印对象的name，class_name属性
print('name:', student.name)
print('class_name: ', student.class_name)

# 在数据库表中更新数据
# 查询并更新数据
session.query(Product).filter(Product.ID == '19558276').update({Product.name: "北京5天4晚自由行，景+酒套餐"})
# 提交即保存到数据库
session.commit()

# 从数据库中删除数据
session.query(Product).filter(Product.ID == '19558276').delete()
# 提交即保存到数据库
session.commit()
# 关闭Session
session.close()
