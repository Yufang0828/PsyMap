# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.http.response import HttpResponse
from PsyMap.util import web


def experiment(request, page):
    ip = web.get_ip_from_request(request)
    return HttpResponse(ip)





