# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.http.response import HttpResponse
from django.shortcuts import render


def account(request, page):

    page = 'PsyMap/home/home.html' if page not in {'login', 'logout', 'profile'} else 'PsyMap/accounts/%s.html' % page
    return render(request, page)

