import pymysql
# 连接mysql8居然不用跟java一样需要参数
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    db="taobao",
)
db.set_charset('utf8mb4')
# 获取数据游标
cur = db.cursor()
# 执行SQL语句，进行查询
sql = 'SELECT * FROM sale_data where 位置 in (%s, %s, %s)'
cur.execute(sql, ("江苏", "浙江", "上海"))
result = cur.fetchall()
for item in result:
    print(item)

# 执行SQL语句，进行删除
sql = 'DELETE FROM sale_data where 价格 < 100'
cur.execute(sql)
# 没有设置在自动提交，需要主动提交，以保存所执行的语句
db.commit()

# 执行SQL语句，把江苏 浙江 上海统一改成江浙沪
sql = 'UPDATE sale_data SET 位置 = %s WHERE 位置 in (%s, %s, %s)'
cur.execute(sql, ("江浙沪", "江苏", "浙江", "上海"))
# 没有设置在自动提交，需要主动提交，以保存所执行的语句
db.commit()

# 执行SQL语句，插入一条新的销售记录
sql = 'INSERT INTO sale_data (宝贝,价格,成交量,卖家,位置) VALUES (%s, %s, %s, %s, %s)'
cur.execute(sql, ("2017夏季妈妈装40-50岁中老年女装连衣裙", "298", "1000", "XXX天猫旗舰店", "北京"))
# 没有设置在自动提交，需要主动提交，以保存所执行的语句
db.commit()
# 关闭游标和数据库连接
cur.close()
db.close()