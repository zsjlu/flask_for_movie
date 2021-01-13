# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:53
# @Author  :robot_zsj
# @File    :index_7.py.py
from flask import Flask

app = Flask(__name__)
# 从配置文件读取（推荐）
app.config.from_pyfile("config/base_setting.py")


@app.route("/")
def hello():
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0')