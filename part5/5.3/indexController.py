# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:57
# @Author  :robot_zsj
# @File    :app_1.py
from flask import Flask, Blueprint, request, make_response

'''
post/index 列表
post/info 详情
post/set 添加
post/ops 操作
'''

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index_page_index():
    return "imooc index page"


@index_page.route("/my")
def hello():
    return "hello, I Love Imooc"


@index_page.route("/get")
def get():
    # var_a = request.args.get("a", "i love imooc")
    req = request.values
    var_a = req['a'] if 'a' in req else ""
    return "request:%s,params:%s,var_a:%s" \
           % (request.method, request.args, var_a)


@index_page.route('/post', methods=["POST"])
def post():
    # var_a = request.form['a'] if 'a' in request.form else ""
    req = request.values
    var_a = req['a'] if 'a' in req else ""
    return "request:%s,params:%s,var_a:%s" \
           % (request.method, request.form, var_a)


@index_page.route("/upload", methods=["POST"])
def upload():
    f = request.files['file'] if 'file' in request.files else None
    return "request:%s,params:%s,f:%s" % \
           (request.method, request.files, f)



