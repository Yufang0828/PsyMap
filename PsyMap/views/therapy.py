# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.http.response import HttpResponse


def therapy(request, page):
    req = request.META
    ip = req.get('HTTP_X_FORWARDED_FOR', req.get('REMOTE_ADDR', 'Unknown'))
    if ',' in ip:
        ip = ip.split(',')[0].strip(' []')
    return HttpResponse(ip)