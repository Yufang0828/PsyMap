# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.http.response import HttpResponse
from django.shortcuts import render


def account(request, page):
    if page not in {'index', 'fill', 'results'}:
        page = 'index'
    return render(request, 'PsyMap/quiz/%s.html' % page)

