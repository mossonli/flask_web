#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'

from flask import Flask, render_template, redirect, flash, session, Response, url_for, request
from forms import LoginForm, RegisterForm, ArtForm, ArtEditForm
from models import User, db, Art
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
import uuid
import time
import os
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "we"
app.config["up_logo"] = os.path.join(os.path.dirname(__file__), "static/uploads")

#定义一个登录的装饰器
def user_login_req(func):
    @wraps(func)
    def login_req(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return login_req


#登录
@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        session["user"] = data["name"]
        flash(u"登录成功！", "ok")
        return redirect("/art/list/1/")
        
    return render_template("login.html", title=u"登录", form=form)


#注册
@app.route("/register/", methods=["GET", "POST"])
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
        return redirect("/login/")
    else:
        flash(u"注册失败，请重新注册", "err")
    return render_template("register.html", title=u"注册", form=form)


#退出
@app.route("/logout/", methods=["GET", "POST"])
@user_login_req
def logout():
    session.pop("user", None)
    return redirect('/login/')
    # return render_template("layout.html", title="登录")


# 修改文件名称
def change_logo_name(name):
    info = os.path.splitext(name)
    # name :时间字符串+唯一字符串+后缀名
    name = str(int(time.time())) + str(uuid.uuid4().hex) + info[-1]
    return name


# 发布文章
@app.route('/art/add/', methods=["GET", "POST"])
@user_login_req
def art_add():
    form = ArtForm()
    if form.validate_on_submit():
        # 上传 logo
        data = form.data
        file = secure_filename(form.logo.data.filename)
        logo = change_logo_name(file)
        if not os.path.exists(app.config["up_logo"]):
            os.makedirs(app.config["up_logo"])
        # 保存文件
        form.logo.data.save(app.config["up_logo"] + '/' + logo)
        # 获取作者
        user = User.query.filter(User.name == session["user"]).first()
        user_id = user.id
        # 保存数据
        art = Art(
            title=data["title"],
            cate=data["cate"],
            user_id=user_id,
            logo=logo,
            content=data["content"],
            addtime=int(time.time())
        )
        db.session.add(art)
        db.session.commit()
        flash(u"发布成功！", "ok")

    return render_template("art_add.html", title="添加文章", form=form)
# 编辑文章
@app.route('/art/edit/<int:id>/', methods=["GET", "POST"])
@user_login_req
def art_edit(id):
    form = ArtEditForm()
    art = Art.query.get_or_404(int(id))
    if request.method == 'GET':
        # 动态获取 文章的内容 复初始值
        form.content.data = art.content
        form.cate.data = art.cate
        form.logo.data = art.logo
    if form.validate_on_submit():
        data = form.data
        # 上传 logo
        file = secure_filename(form.logo.data.filename)
        logo = change_logo_name(file)
        if not os.path.exists(app.config["up_logo"]):
            os.makedirs(app.config["up_logo"])
        # 保存文件
        form.logo.data.save(app.config["up_logo"] + "/" + logo)
        art.logo = logo
        art.title = data["title"]
        art.content = data["content"]
        art.cate = data["cate"]
        db.session.add(art)
        db.session.commit()
        flash(u"文章编辑成功", "ok")

    return render_template("art_edit.html", form=form, title=u"编辑文章", art=art)
    
# 删除文章
@app.route('/art/del/<int:id>/', methods=["GET", "POST"])
@user_login_req
def art_del(id):
    art = Art.query.get_or_404(int(id))
    db.session.delete(art)
    db.session.commit()
    flash(u"删除《%s》成功" % art.title, "ok")
    return redirect("/art/list/1/")

    
# 文章列表
@app.route('/art/list/<int:page>/', methods=["GET", "POST"])
@user_login_req
def art_list(page=None):
    if page is None:
        page = 1
    user = User.query.filter(User.name == session["user"]).first()
    user_id = user.id
    page_data = Art.query.filter(Art.user_id == user_id).order_by(Art.addtime.desc()).paginate(page=page, per_page=1)
    cate = [(1, u"科技"), (2, u"搞笑"), (3, u"军事")]
    return render_template("art_list.html", title="文章列表", page_data=page_data, cate=cate)


@app.route('/captcha/', methods=['GET'])
def codes():
    from captcha import Captcha
    c = Captcha()
    info = c.create_captcha()
    image = os.path.join(os.path.dirname(__file__), "static/captcha/" + info["image_name"])
    with open(image, "rb") as fd:
        image = fd.read()
    session["captcha"] = info["captcha"]
    return Response(image, mimetype="jpeg")
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)