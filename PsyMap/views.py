from django.shortcuts import render
from django.http import HttpResponse


def home(request, page='home'):
    if page not in {'home', 'about'}:
        page = 'home'
    return render(request, 'PsyMap/home/%s.html' % page)


def account(request, page):
    pass


def admin(request, page):
    pass


def common(request, page):
    pass


def exp(request, page):
    pass


def quiz(request, page):
    if page not in {'index', 'fill', 'results'}:
        page = 'index'
    return render(request, 'PsyMap/quiz/%s.html' % page)


def sns(request, page):
    pass


def api(request):
    echostr = request.REQUEST.get('echostr')
    return HttpResponse(echostr)