# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:57
# @Author  :robot_zsj
# @File    :app_1.py
from flask import Flask, Blueprint
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



