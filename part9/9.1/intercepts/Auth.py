# -*- coding: utf-8 -*-
# @Time    :2021/2/5 22:02
# @Author  :robot_zsj
# @File    :Auth.py
from application import app

@app.before_request
def before_request():
    app.logger.info("-------before--------")
    return

@app.after_request
def after_request(response):
    app.logger.info("-------after--------")
    return response