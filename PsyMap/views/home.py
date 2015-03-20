# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.shortcuts import render


def home(request, page='home'):
    if page not in {'home', 'about'}:
        page = 'home'
    print request.session.get('nickname')
    return render(request, 'PsyMap/home/%s.html' % page)
