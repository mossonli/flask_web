#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'

from flask import Flask, render_template, redirect, flash
from forms import LoginForm, RegisterForm, ArtForm
from models import User, db
from werkzeug.security import generate_password_hash
import time


app = Flask(__name__)
app.config["SECRET_KEY"] = "we"

#登录
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


#注册
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        # 数据存储
        user = User(
             name=data["name"],
             pwd=generate_password_hash(data["pwd"]),
             addtime=int(time.time())
        )
        db.session.add(user)
        db.session.commit()
        # 绘画的闪现
        flash(u"注册成功请登录", "ok")
        return redirect("/login")
    else:
        flash(u"注册失败，请重新注册", "err")
        return redirect("/register")
    return render_template("register.html", title="注册", form=form)


#退出
@app.route("/logout", methods=["GET", "POST"])
def logout():
    return render_template("logout.html", title="登录")

# 发布文章
@app.route('/art/add', methods=["GET", "POST"])
def art_add():
    form = ArtForm()
    return render_template("art_add.html", title="添加文章", form=form)
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