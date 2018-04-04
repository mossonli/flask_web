#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # flask-sqlalchemy 的版本 不要超过2.0
from werkzeug.security import check_password_hash
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@********:3306/artcms?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pwd = db.Column(db.String(100), nullable=False)
    addtime = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)
    

class Art(db.Model):
    __tablename__ = "art"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cate = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    logo = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Art %r>" % self.title