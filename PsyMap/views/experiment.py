# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.http.response import HttpResponse


def experiment(request, page):
    print request.environ
    req = request.environ

    ip_addr = req.get('HTTP_X_FORWARDED_FOR', req.get('REMOTE_ADDR', 'Unknown'))
    print ip_addr
    ip_addr = ip_addr.split(',')[0].strip()
    idx = ip_addr.rindex(':') if ':' in ip_addr else len(ip_addr)
    ip_addr = ip_addr[:idx].strip('[]')

    import ipaddr
    ip = ipaddr.IPAddress(ip_addr)

    request.session['nickname'] = ip_addr
    return HttpResponse(ip)
