__author__ = 'Peter'

from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',

    url(r'^$',                      views.home),                                # home page
    url(r'^home/(.*)$',             views.home),                                # home page

    url(r'^account/(.*)$',          views.account),                             # account

    url(r'^experiment/(.*)$',       views.exp),                                 # experiment
    url(r'^quiz/(.*)$',             views.quiz),                                # quiz

    url(r'^knowledge/(.*)$',        views.quiz),                                # knowledge
    url(r'^therapy/(.*)$',          views.quiz),                                # therapy

    url(r'^sns/(.*)$',              views.sns),                                 # sns

    url(r'^api/$',                   views.api),                                 # api
)