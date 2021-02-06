# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:57
# @Author  :robot_zsj
# @File    :app_1.py
from flask import Flask, Blueprint, request, make_response, jsonify, render_template
from sqlalchemy import text
from application import db
from common.models.user import User
'''
post/index 列表
post/info 详情
post/set 添加
post/ops 操作
'''

index_page = Blueprint("index_page", __name__)

# 默认查找当前目录下templates目录下的html文件
@index_page.route("/")
def index():
    ## 传值
    name = "imooc1"
    context = {"name": name}
    context['user'] = {"nickname": "zsj", "qq": "xxx", "home_page": "http://www.baidu.com"}
    context['num_list'] = [1, 2, 3, 4, 5]

    # 传输数据库
    sql = text("select * from `user`")
    result = db.engine.execute(sql)



    result = User.query.all()
    context['result'] = result
    return render_template("index.html", **context)

