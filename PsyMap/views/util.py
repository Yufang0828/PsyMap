# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'


from django.shortcuts import render_to_response
from django.template import RequestContext
from PsyMap.util import *

page = 'PsyMap/common/info.html'


def handler404(request):
    r = {'err': 404, 'msg': ':-| 找不到您访问的页面~', 'redirect': web.get_prev_uri(request)}
    response = render_to_response(page, r, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    r = {'err': 500, 'msg': ':-( 我们的系统出错了。。。', 'redirect': web.get_prev_uri(request)}
    response = render_to_response(page, r, context_instance=RequestContext(request))
    response.status_code = 500
    return response


def view_info(request, msg, redirect=None):
    r = {'msg': msg, 'redirect': redirect or web.get_prev_uri(request)}
    response = render_to_response(page, r, context_instance=RequestContext(request))
    return response