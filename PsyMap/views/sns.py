# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.shortcuts import render


def index(request, page=None):
    page = 'index'
    return render(request, 'PsyMap/sns/%s.html' % page)


def psych(request, site='weibo', page=None):
    if site not in {'weibo'}:  #, 'renren', 'douban'
        return index(request)

    return render(request, 'PsyMap/sns/%s.html' % site)

