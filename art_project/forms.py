#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask_wtf import FlaskForm
from wtforms import StringFiled, PasswordFeild, SubmitFeild
"""
登录表单：账户、密码、登录按钮
"""
class LoginForm(FlaskForm):
    name = u"帐号",
    validdators = [],
    description = u"帐号",
    render_kw = {
        "class": "form-control",
        "placeholder":
    }
"""
注册表单：账户、密码、确认密码、验证码、注册按钮
"""

"""
发布文章：标题、分类、封面、内容、发布文章按钮
"""