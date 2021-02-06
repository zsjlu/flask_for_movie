# -*- coding: utf-8 -*-
# @Time    :2021/2/6 13:32
# @Author  :robot_zsj
# @File    :DataHelper.py
import datetime

def getCurrentTime(frm="%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.now()
    return dt.strftime(frm)