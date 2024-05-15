from flask import Flask,render_template, request,redirect,url_for
from mysql_util import MysqlUtil
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


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
        sql = "INSERT INTO user(username,password,email) \
        VALUES ('%s', '%s', '%s')" % (username,password,email) # 插入数据的SQL语句

        product_list = db.insert(sql)  # 获取多条记录

        print(product_list)

        # insert_data(username, password, email)
        # return render_template("index.html")
        return redirect(url_for('index'))

    else: #GET
         return render_template("register.html")


app.run(debug=True)