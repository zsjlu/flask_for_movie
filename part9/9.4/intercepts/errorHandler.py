# -*- coding: utf-8 -*-
# @Time    :2021/2/5 22:10
# @Author  :robot_zsj
# @File    :errorHandler.py
from application import app

@app.errorhandler( 404 )
def error_404( e ):
    return "404 not found"