#!/usr/bin/env python
# -*- coding: utf-8 -*-

#flask_bootstrap:
#http://www.jb51.net/article/110841.htm

from flask import Flask, request, redirect
from gevent.wsgi import WSGIServer
from flask import render_template
from flask_bootstrap import Bootstrap
import cx_Oracle
app = Flask(__name__)

#对bootstrap进行初始化
bootstrap=Bootstrap(app)

# @app.route("/get_github_user",methods=['GET'])
@app.route("/",methods=['GET'])
def get_github_user():
    conn = cx_Oracle.connect('study','Zwd525414', '202.115.82.8:1521/pdborcl')
    cur = conn.cursor()
    # where id=:p1",{"p1":1})
    sql = "SELECT id,name,class,github_username,update_date FROM is_analysis_studyinfo"
    cur.execute(sql)
    students = cur.fetchall()
    conn.close()
    return render_template('list.html',students=students)

# 普通函数,返回学号对应的学生姓名和github账号
def get_one_user(stu_id):
    conn = cx_Oracle.connect('study','Zwd525414', '202.115.82.8:1521/pdborcl')
    cur = conn.cursor()
    sql = "SELECT name,github_username FROM is_analysis_studyinfo where id=:id"
    res = cur.execute(sql,{"id":stu_id})
    name=""
    github_username=""
    for row in res:
        name=row[0]
        github_username=row[1]
    conn.close()
    return name, github_username

@app.route("/update_github_user/<string:stu_id>",methods=['GET','POST'])
def update_github_user(stu_id):
    if request.method == "POST": #如果是POST方式,表示在修改页面按下了"修改"按钮.
        username = request.form.get('GitHubUserName')
        conn = cx_Oracle.connect('study', 'Zwd525414', '202.115.82.8:1521/pdborcl')
        cur = conn.cursor()
        username=username.strip()
        if username != '':
            cur.execute("UPDATE is_analysis_studyinfo SET github_username=:username,update_date=sysdate WHERE id=:id",
                        {"username":username, "id":stu_id})
        else: #如果没有用户名,要清空日期
            cur.execute("UPDATE is_analysis_studyinfo SET github_username=NULL ,update_date=NULL WHERE id=:id",
                        {"id":stu_id})
        conn.commit() # 提交是必须的
        conn.close()
        return redirect('/') #返回主页
    else: # 如果是GET方式访问接口,返回修改用户名的页面
        realname, username=get_one_user(stu_id)
        return render_template('update.html',stu_id=stu_id,GitHubUserName=username,realname=realname)

if __name__ == "__main__":
    #使用https方式将使抓出的IP包无法直接观看.
    #app.run(host="0.0.0.0", port=1522, debug=False) # ,ssl_context='adhoc')
    WSGIServer(('0.0.0.0',1522),app).serve_forever() #异步非堵塞实现