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

    url(r'^quiz/fill/(?P<grp_id>\w+)/(?P<quiz_id>\w+)$',             views.quiz.fill),                                # quiz
    url(r'^quiz/index$',             views.quiz.index),                                # quiz

    url(r'^account/(.*)$',          views.account),                             # account

    url(r'^experiment/(.*)$',       views.experiment),                          # experiment


    url(r'^knowledge/(.*)$',        views.knowledge),                           # knowledge
    url(r'^therapy/(.*)$',          views.therapy),                             # therapy

    url(r'^sns/(.*)$',              views.sns),                                 # sns

    url(r'^api/wechat$',            views.api_wechat),                          # wechat api
)