# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:57
# @Author  :robot_zsj
# @File    :app_1.py
from flask import Flask, Blueprint

app = Flask(__name__)

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index_page_index():
    return "index page"


app.register_blueprint(index_page, url_prefix="/imooc")


@app.route("/")
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
