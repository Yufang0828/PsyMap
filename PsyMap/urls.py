# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.conf.urls import patterns, url, include
from django.contrib import admin

import views
urlpatterns = patterns(
    '',

    (r'^admin/', include(admin.site.urls)),                                     # admin page

    url(r'^$',                      views.home),                                # home page
    url(r'^home/(.*)$',             views.home),                                # home page

    url(r'^quiz/index/(?P<page>\w*)$',                     views.quiz.index),   # quiz index
    url(r'^quiz/fill/(?P<grp_id>\d+)/(?P<quiz_id>\w+)$',   views.quiz.fill),    # quiz fill
    url(r'^quiz/fill/(?P<quiz_id>\w+)$',                   views.quiz.fill),    # quiz fill
    url(r'^quiz/submit$',            views.quiz.submit),                        # quiz submit
    url(r'^quiz/result$',            views.quiz.result),                        # quiz result

    url(r'^accounts/login$',                                views.accounts.login),                       # account
    url(r'^accounts/logout$',                               views.accounts.logout),                      # account
    url(r'^accounts/callback/(?P<site>\w+)$',               views.accounts.callback),                    # account

    url(r'^sns/(.*)$',              views.sns),                                 # sns


    url(r'^experiment/(.*)$',       views.experiment),                          # experiment

    url(r'^knowledge/(.*)$',        views.knowledge),                           # knowledge
    url(r'^therapy/(.*)$',          views.therapy),                             # therapy

    url(r'^api/wechat$',            views.api_wechat),                          # wechat api
)
