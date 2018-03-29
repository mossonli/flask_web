#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask import Flask
from flask_sqlalchemy import SQLALCHEMY


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_UIL"] = "mysql+pymysql://root:lilu136782643@58.87.88.120:3306/artcrms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLALCHEMY(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pwd = db.Column(db.String(100), nullable=False)
    addtime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.name


class Art(db.Model):
    __tablename__ = "art"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cate = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    logo = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    addtime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Art %r>" % self.title