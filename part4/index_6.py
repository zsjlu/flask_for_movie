# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:52
# @Author  :robot_zsj
# @File    :index_6.py
from flask import Flask

app = Flask(__name__)
# 从环境变量设置 export ops_config/set ops_config
app.config.from_envvar("ops_config")


@app.route("/")
def hello():
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
