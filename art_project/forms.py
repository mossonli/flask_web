#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'mosson'
from flask_wtf import FlaskForm
# import flask.ext.wtf
from werkzeug.security import check_password_hash
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from models import User
from flask import session as form_session
"""
登录表单：账户、密码、登录按钮
"""


class LoginForm(FlaskForm):
    name = StringField(
        label=u"帐号",
        validators=[
            DataRequired(u"帐号不能为空")
        ],
        description=u"帐号",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入账户"
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[
            DataRequired(u"密码不能为空！")
        ],
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
    def validate_name(self, field):
        name = field.data  # 前端页面输入的name
        user = User.query.filter(User.name == self.name.data).first()
        if not user:
            raise ValidationError(u"用户不存在")
        # self.__validate_pwd(field)

    # 检测用户输入的密码 
    def validate_pwd(self, field):
        pwd = field.data  # 表示前端输入 密码
        print(pwd)
        print(self.name.data)
        user = User.query.filter(User.name == self.name.data).first()
        if not user:
            raise ValidationError(u"请先查看用户名是否正确!!")
        if not user.check_pwd(pwd):
                raise ValidationError(u"密码不正确！")


"""
注册表单：账户、密码、确认密码、验证码、注册按钮
"""
class RegisterForm(FlaskForm):
    name = StringField(
        label=u"帐号",
        validators=[
            DataRequired(u"帐号不能为空！")
        ],
        description=u"帐号",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入账户"
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[
            DataRequired(u"密码不能为空！")
        ],
        description=u"密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码"
        }
    )
    repwd = PasswordField(
        label=u"确认密码",
        validators=[
            DataRequired(u"确认密码不能为空！"),
            EqualTo("pwd", message=u"两个密码不一致！")
        ],
        description=u"确认密码",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入密码"
        }
    )
    captcha = StringField(
        label=u"验证码",
        validators=[
            DataRequired(u"验证码不能为空")
        ],
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
    # 自定义字段验证规则：vaildate_字段名
    def validate_name(self, field):
        name = field.data
        user = User.query.filter(name == name).count()
        if user > 0:
            raise ValidationError(u"账户已经存在不能重复注册！")
    # 自定义验证码验证
    def validate_captcha(self, field):
        captcha = field.data
        if not form_session["captcha"]:
            raise ValidationError(u"非法操作")
        if form_session["captcha"].lower() != captcha.lower():
            raise ValidationError(u"验证码不正确")  
    
        
"""
发布文章：标题、分类、封面、内容、发布文章按钮
"""
class ArtForm(FlaskForm):
    title = StringField(
        label=u"标题",
        validators = [
            DataRequired(u"标题不能为空")
        ],
        description=u"标题",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入标题"
        }
    )
    cate = SelectField(
        label=u"分类",
        validators = [
            DataRequired(u"分类不能为空")
        ],
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
        validators = [
            DataRequired(u"封面不能为空")
        ],
        description=u"封面",
        render_kw={
            "class": "form-control-file",
        }
    )
    content = TextAreaField(
        label=u"内容",
        validators = [
            DataRequired(u"内容不能为空")
        ],
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


"""
编辑文章：标题、分类、封面、内容、发布文章按钮
"""
class ArtEditForm(FlaskForm):
    id = IntegerField(
        label=u"编号",
        validators = [
            DataRequired(u"编号不能为空")
        ]
    )
    title = StringField(
        label=u"标题",
        validators = [
            DataRequired(u"标题不能为空")
        ],
        description=u"标题",
        render_kw={
            "class": "form-control",
            "placeholder": u"请输入标题"
        }
    )
    cate = SelectField(
        label=u"分类",
        validators = [
            DataRequired(u"分类不能为空")
        ],
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
        validators = [
            DataRequired(u"封面不能为空")
        ],
        description=u"封面",
        render_kw={
            "class": "form-control-file",
        }
    )
    content = TextAreaField(
        label=u"内容",
        validators = [
            DataRequired(u"内容不能为空")
        ],
        description=u"内容",
        render_kw={
            "style": "form-control",
            "id": "content"
        }
    )
    
    submit = SubmitField(
        label=u"编辑文章",
        render_kw={
            "class": "btn btn-primary",
        }
    )