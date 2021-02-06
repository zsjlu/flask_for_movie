# -*- coding: utf-8 -*-
# @Time    :2021/2/5 23:52
# @Author  :robot_zsj
# @File    :member.py.py
from application import app
from flask import Flask, Blueprint, request, make_response, jsonify, render_template

member_page = Blueprint("member_page", __name__)

@member_page.route("/reg")
def reg():
    return render_template("member/reg.html")

@member_page.route("/login")
def login():
    return render_template("member/login.html")