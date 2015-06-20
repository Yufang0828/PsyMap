# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.conf.urls import patterns, url, include
from django.contrib import admin

import views

urlpatterns = patterns(
    '',

    (r'^admin/', include(admin.site.urls)),               # admin page

    url(r'^api/wechat$',                                  views.api_wechat),         # wechat api

    url(r'^$',                                            views.home),               # home page
    url(r'^home/(.*)$',                                   views.home),               # home page

    url(r'^quiz/index/(?P<page>\w*)$',                    views.quiz.index),         # quiz index
    url(r'^quiz/fill/(?P<grp_id>\d+)/(?P<quiz_id>\w+)$',  views.quiz.fill),          # quiz fill
    url(r'^quiz/fill/(?P<quiz_id>\w+)$',                  views.quiz.fill),          # quiz fill
    url(r'^quiz/submit$',                                 views.quiz.submit),        # quiz submit
    url(r'^quiz/result$',                                 views.quiz.result),        # quiz result

    url(r'^accounts/login$',                              views.accounts.login),     # account login
    url(r'^accounts/logout$',                             views.accounts.logout),    # account logout
    url(r'^accounts/callback/(?P<site>\w+)$',             views.accounts.callback),  # account link callback

    url(r'^emotion/index/$',                             views.emotion.index),    # emotion check in

    # TODO: delete these two lines if not needed
    # url(r'^emotion/success/(?P<lat>\d+\.\d+)/(?P<long>\d+\.\d+)$' ,      views.emotion.success),
    # url(r'^emotion/emotion/(?P<lat>\d+\.\d+)/(?P<long>\d+\.\d+)/(?P<emotion>\w+)', views.emotion.emotion),

    url(r'^sns/index/(?P<page>\w*)$',                     views.sns.index),          # sns index
    url(r'^sns/psych/(?P<site>\w*)/(?P<page>\w*)$',       views.sns.psych),          # sns psych

    url(r'^experiment/(.*)$',       views.experiment.index),                          # experiment

    url(r'^knowledge/(.*)$',        views.knowledge.index),                           # knowledge

    url(r'^therapy/(.*)$',          views.therapy.index),                             # therapy
)
