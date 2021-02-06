# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:57
# @Author  :robot_zsj
# @File    :app_1.py
import os

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)

manager = Manager( app )

# 放入到配置文件中
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask_for_movie:flask_for_movie@47.115.163.10/' \
#                                         'flask_for_movie'
# 之后就通过以下命令来设置环境
# linux export ops_config=local|production
# windwos set ops_config=local|production
app.config.from_pyfile("config/base_setting.py")
if "ops_config" in os.environ:
    app.config.from_pyfile("config/%s_setting.py" % ( os.environ['ops_config']))

app.logger.info("+++++++++++++++++++++")

db = SQLAlchemy(app)

