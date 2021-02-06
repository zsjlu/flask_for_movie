# -*- coding: utf-8 -*-
# @Time    :2021/2/6 17:56
# @Author  :robot_zsj
# @File    :UserService.py.py
import random, string,hashlib,base64


class UserService:

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))

    @staticmethod
    def genePwd(pwd, salt):
        m = hashlib.md5()
        str = "%s-%s"%(base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()