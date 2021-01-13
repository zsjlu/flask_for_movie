# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:50
# @Author  :robot_zsj
# @File    :index_5.py
from flask import Flask

app = Flask(__name__)
# 从模块获取
app.config.from_object("config.base_setting")


@app.route("/")
def hello():
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0')