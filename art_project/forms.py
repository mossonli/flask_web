#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask.ext.wtf import Form
# import flask.ext.wtf
from wtforms import StringField, PasswordField, SubmitField
"""
登录表单：账户、密码、登录按钮
"""


class LoginForm(Form):
    name = StringField(
        label=u"帐号",
        validators=[],
        description=u"帐号",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入账户"
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码"
        }
    )
    subbit = SubmitField(
        label=u"登录",
        render_kw={
            "class": "btn btn-primary",
        }
    )
    

"""
注册表单：账户、密码、确认密码、验证码、注册按钮
"""

"""
发布文章：标题、分类、封面、内容、发布文章按钮
"""