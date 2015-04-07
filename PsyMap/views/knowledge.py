# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.http.response import HttpResponse
from util import view_info


def index(request, page):
    msg = ['感谢您访问“心理知识”功能，该模块正在开发中。'
           '请您关注我们的微博、微信，功能有更新时我们会通知您~']
    msg = '\n'.join(msg)

    return view_info(request, msg=msg)