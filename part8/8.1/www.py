# -*- coding: utf-8 -*-
# @Time    :2021/1/17 23:23
# @Author  :robot_zsj
# @File    :www.py.py
from application import app
from controllers.index  import index_page

app.register_blueprint(index_page, url_prefix="/")
