# -*- coding: utf-8 -*-
# @Time    :2021/1/13 21:44
# @Author  :robot_zsj
# @File    :index_1.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"