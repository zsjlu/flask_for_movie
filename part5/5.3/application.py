# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:57
# @Author  :robot_zsj
# @File    :app_1.py
from flask import Flask, Blueprint
from indexController import index_page

app = Flask(__name__)

app.register_blueprint(index_page, url_prefix="/imooc")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
