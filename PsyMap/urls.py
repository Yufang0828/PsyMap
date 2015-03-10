__author__ = 'Peter'

from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^home/(.*)$',      views.home),                                # home page

    url(r'^account/(.*)$',   views.account),                             # account
    url(r'^exp/(.*)$',       views.exp),                                 # exp
    url(r'^quiz/(.*)$',      views.quiz),                                # quiz
    url(r'^sns/(.*)$',       views.sns),                                 # sns

    url(r'^api/$',           views.api),                                 # api
)