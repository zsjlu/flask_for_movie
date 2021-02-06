# -*- coding: utf-8 -*-
# @Time    :2021/1/17 23:23
# @Author  :robot_zsj
# @File    :www.py.py
from application import app
from controllers.index  import index_page
from controllers.member  import member_page

app.register_blueprint(index_page, url_prefix="/")
app.register_blueprint(member_page, url_prefix="/member")


# toolbar使用
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension( app )

"""
拦截器处理
"""
from intercepts.Auth import *
from intercepts.errorHandler import *