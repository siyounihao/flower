import pymysql
connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '123456',  # 数据库密码
    db = 'hello_database',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor
)

print(connectiont)
cursor = connectiont.cursor() # 获取游标对象
sql = """
create table user_table(
id int(8) auto_increment primary key,
username varchar(30) not null,
password varchar(30) not null,
email varchar(30) not null,
create_time datetime);
"""

cursor.execute(sql) # 执行SQL语句
cursor.close()      # 关闭游标
connectiont.close() # 关闭连接