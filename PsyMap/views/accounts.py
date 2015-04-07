# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'


from django.shortcuts import render
from django.contrib import auth

from PsyMap.models import UserLink

from api_hub import hub
from PsyMap.util import *


def login(request):
    prev = web.get_prev_uri(request, local_only=True)
    request.session['redirect'] = prev
    page = 'PsyMap/accounts/login.html'
    return render(request, page)


def logout(request):
    auth.logout(request)
    page = 'PsyMap/home/home.html'
    return render(request, page)


def callback(request, site):
    site = UserLink.check_site(site)
    if site is None:
        return login(request)

    code = request.GET.get('code') or request.POST.get('code')
    err = None
    try:
        token, uid, err = hub.link(site.alias, code)
        if (err is None or len(err) == 0) and len(token) > 0 and len(uid) > 0:
            token, uid = token[0], uid[0]
            u_link = UserLink.link(site.code, uid, token)
            if u_link is not None:
                u_link.backend = 'django.contrib.auth.backends.ModelBackend'
                auth.login(request, u_link)
        else:
            raise RuntimeError('Fail to get access_token information for %s!' % site.alias)
    except Exception as e:
        print e
        err = {} if err is None else err
        err['PsyMap Error /accounts/login'] = e

    r = {
        'site': site,
        'err': err,
        'redirect': request.session.pop('redirect', domain)
    }
    page = 'PsyMap/accounts/link.html'
    return render(request, page, r)
