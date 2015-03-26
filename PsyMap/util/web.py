# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'


def get_ip_from_request(request):
    req = request.environ
    ip_addr = req.get('HTTP_X_FORWARDED_FOR', req.get('REMOTE_ADDR', '0.0.0.0'))
    ip_addr = ip_addr.split(',')[0].strip()
    idx = ip_addr.rindex(':') if ':' in ip_addr else len(ip_addr)
    ip = ip_addr[:idx].strip('[]')
    return ip