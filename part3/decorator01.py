# -*- coding: utf-8 -*-
# @Time    :2021/1/12 5:09
# @Author  :robot_zsj
# @File    :decorator01.py
def use_logging(func):
    def wrapper(*args, **kwargs):
        print("[debug]%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@use_logging
def bar():
    print('i am bar')


# bar = use_logging(bar)
# bar()

bar()