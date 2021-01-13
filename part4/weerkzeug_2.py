# -*- coding: utf-8 -*-
# @Time    :2021/1/13 22:15
# @Author  :robot_zsj
# @File    :weerkzeug_2.py
from werkzeug import Response, Request


class Shortly(object):
    def __call__(self, environ, start_response):
        # start_response('200 OK', [('Content-Type', 'text/plain')])
        # return [b'hello world']
        request = Request(environ)
        text = 'hellow, %s' % (request.args.get('a', 'i love imooc'))
        response = Response(text, mimetype="text/plain")
        return response(environ, start_response)


if __name__ == '__main__':
    from werkzeug.serving import run_simple

    app = Shortly()
    run_simple('0.0.0.0', 5000, app)
