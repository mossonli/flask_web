#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask.ext.wtf import Form
# import flask.ext.wtf
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField
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
    submit = SubmitField(
        label=u"登录",
        render_kw={
            "class": "btn btn-primary",
        }
    )
    

"""
注册表单：账户、密码、确认密码、验证码、注册按钮
"""
class RegisterForm(Form):
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
    repwd = PasswordField(
        label=u"确认密码",
        validators=[],
        description=u"确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码"
        }
    )
    code = StringField(
        label=u"验证码",
        validators=[],
        description=u"验证码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入验证码"
        }
    )
    submit = SubmitField(
        label=u"注册",
        render_kw={
            "class": "btn btn-primary",
        }
    )
"""
发布文章：标题、分类、封面、内容、发布文章按钮
"""
class ArtForm(Form):
    title = StringField(
        label=u"标题",
        validators=[],
        description=u"标题",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入标题"
        }
    )
    cate = SelectField(
        label=u"分类",
        validators=[],
        description=u"分类",
        choices=[(1, u"科技"), (2, u"搞笑"), (3, u"军事")],
        default=3,
        coerce=int,
        render_kw={
            "class": "form-control",
        }
    )
    logo = FileField(
        label=u"封面",
        validators=[],
        description=u"封面",
        render_kw={
            "class": "form-control-file",
        }
    )
    content = TextAreaField(
        label=u"内容",
        validators=[],
        description=u"内容",
        render_kw={
            "style": "form-control",
            "id": "content"
        }
    )
    
    submit = SubmitField(
        label=u"发布文章",
        render_kw={
            "class": "btn btn-primary",
        }
    )