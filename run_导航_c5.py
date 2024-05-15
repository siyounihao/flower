from flask import Flask,render_template, request,redirect,url_for,session
from mysql_util import MysqlUtil
import random
app = Flask(__name__)
app.secret_key = 'mrsoft12345678' # 设置秘钥

@app.route('/')
def index():
    # categorys = [
    #     {
    #         "id": 1,
    #         "cname": "女装男装",
    #     },
    #     {
    #         "id": 2,
    #         "cname": "鞋靴箱包",
    #     },
    #     {
    #         "id": 3,
    #         "cname": "运动户外",
    #     },
    # ]

    db = MysqlUtil()
    sql = 'SELECT * FROM category'
    categorys = db.fetchall(sql)  # 获取多条记录
    return render_template("/test/nav.html", categorys=categorys)


@app.route('/register', methods=['GET','POST'])
def register():

    if (request.method == "POST"):
        username = request.form['name']
        password = request.form['password']
        email = request.form['email']

        print(username)
        print(password)
        print(email)


        db = MysqlUtil()

        id = "%20d" % random.randint(0,1000000000)
        sql = "INSERT INTO user(id, username,password,email) \
        VALUES ('%s', '%s', '%s', '%s')" % (id, username, password, email)  # 插入数据的SQL语句

        product_list = db.insert(sql)  # 获取多条记录

        print(product_list)

        # insert_data(username, password, email)
        # return render_template("index.html")
        return redirect(url_for('index'))

    else: #GET
         return render_template("/test/register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if (request.method == "POST"):
        print("ok")
        username = request.form['username']
        password_candidate = request.form['password']
        print(username)
        sql = "SELECT * FROM user  WHERE username = '%s'" % (username)  # 根据用户名查找user表中记录
        db = MysqlUtil()  # 实例化数据库操作类
        result = db.fetchone(sql)  # 获取一条记录
        print(password_candidate)
        print(result)
        db_password = result['password']  # 用户填写的密码
        if password_candidate == db_password:
            # 写入session
            session['logged_in'] = True
            session['username'] = username

            # return "登录成功"# 跳转到控制台
            return redirect(url_for('index'))
        else:
            print("密码错误")
            return render_template("login.html")

    else: #GET
         return render_template("/test/login.html")

@app.route('/logout')
def logout():
    session.clear() # 清除Session
    return redirect(url_for('index'))

app.run(debug=True)