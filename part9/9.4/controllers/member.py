# -*- coding: utf-8 -*-
# @Time    :2021/2/5 23:52
# @Author  :robot_zsj
# @File    :member.py.py
from application import app, db
from flask import Flask, Blueprint, request, make_response, jsonify, render_template
from common.libs.Helper import ops_renderJSON, ops_renderErrJSON
from common.libs.DataHelper import getCurrentTime
from common.models.user import User1
from common.libs.UserService import UserService

member_page = Blueprint("member_page", __name__)


@member_page.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("member/reg.html")

    req = request.values
    login_name = req["login_name"] if "login_name" in req else ""
    login_pwd = req["login_pwd"] if "login_pwd" in req else ""
    login_pwd2 = req["login_pwd2"] if "login_pwd2" in req else ""

    if login_name is None or len(login_name) < 1:
        return ops_renderErrJSON(msg="请输入正确的登陆用户名~~")
    if login_pwd is None or len(login_pwd) < 6:
        return ops_renderErrJSON(msg="请你输入正确的登陆秘密，并且不能小于6个字符~~")
    if login_pwd != login_pwd2:
        return ops_renderErrJSON(msg="请确认你的登陆秘密是否一致~~")

    user_info = User1.query.filter_by(login_name=login_name).first()
    if user_info:
        return ops_renderErrJSON(msg="登陆用户名被注册，请换一个~~")

    model_user = User1()
    model_user.login_name = login_name
    model_user.nickname = login_name
    model_user.login_salt = UserService.geneSalt(8)
    model_user.login_pwd = UserService.genePwd(login_pwd, model_user.login_salt)
    model_user.created_time = model_user.updated_time = getCurrentTime()
    db.session.add(model_user)
    db.session.commit()
    return ops_renderJSON(msg="注册成功~~")


@member_page.route("/login")
def login():
    return render_template("member/login.html")
