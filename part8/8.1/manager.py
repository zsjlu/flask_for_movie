# -*- coding: utf-8 -*-
# @Time    :2021/1/17 23:23
# @Author  :robot_zsj
# @File    :manager.py.py
from application import app, db
from www import *

if __name__ == '__main__':
    # from common.models.user import User
    # db.create_all()

    app.run(host='0.0.0.0', debug=True)
