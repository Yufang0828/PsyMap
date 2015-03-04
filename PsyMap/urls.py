__author__ = 'Peter'

from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '', url(r'^index/$', views.index, name='index'),   # index page 1
)