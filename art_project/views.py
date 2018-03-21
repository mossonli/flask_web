#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'

from flask import Flask, render_template, redirect
app = Flask(__name__)


#登录
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


#注册
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html", title="注册")


#退出
@app.route("/logout", methods=["GET", "POST"])
def logout():
    return render_template("logout.html", title="登录")

# 发布文章
@app.route('/art/add', methods=["GET", "POST"])
def art_add():
    return render_template("art_add.html", title="添加文章")
# 编辑文章
@app.route('/art/edit/<int:id>', methods=["GET", "POST"])
def art_edit(id):
    return render_template("art_edit.html")
# 删除文章
@app.route('/art/del/<int:id>', methods=["GET", "POST"])
def art_del(id):
    return redirect("/art/list")

    
# 文章列表
@app.route('/art/list', methods=["GET", "POST"])
def art_list():
    return render_template("art_list.html", title="文章列表")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)