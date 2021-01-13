# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:57
# @Author  :robot_zsj
# @File    :app_1.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'hello'

@app.route("/my")
def my():
    return 'my'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)