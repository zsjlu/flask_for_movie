# -*- coding: utf-8 -*-
# @Time    :2021/2/5 21:32
# @Author  :robot_zsj
# @File    :base_setting.py.py
from config.base_setting import *

DEBUG = False

RELEASE_PATH = "/home/flask_for_movie/release_version"

SQLALCHEMY_DATABASE_URI = 'mysql://flask_for_movie:flask_for_movie@47.115.163.10/' \
                          'flask_for_movie'

DOMAIN = {
    "www": "http://47.115.163.10:82"
}