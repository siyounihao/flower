import pymysql
connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '',  # 数据库密码
    db = 'new_shop',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)
# 数据列表
data = [
        ("3",'花','13','9.9','/static/images/img-1.jpg'),
        ("4",'花','13','9.9','/static/images/img-2.jpg'),
        ("5",'花','13','9.9','/static/images/img-3.jpg'),
        ("6",'花','13','9.9','/static/images/img-4.jpg'),
        ("7",'花','13','9.9','/static/images/img-5.jpg'),
        ("8",'花','13','9.9','/static/images/img-6.jpg'),

        ]
cursor = connectiont.cursor() # 获取游标对象
try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into product_temp(id,pname,old_price,new_price,images) values (%s,%s,%s,%s,%s)", data)
    # 提交数据
    connectiont.commit()
except:
    # 发生错误时回滚
    print("发生错误时回滚")
    connectiont.rollback()

print("ok")
connectiont.commit()
cursor.close()      # 关闭游标
connectiont.close() # 关闭连接
