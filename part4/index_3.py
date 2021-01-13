# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:45
# @Author  :robot_zsj
# @File    :index_3.py.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)