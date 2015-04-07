# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.conf.urls import patterns, include, url

handler404 = 'PsyMap.views.handler404'
handler500 = 'PsyMap.views.handler500'

urlpatterns = patterns(
    '',
    url(r'^PsyMap/', include('PsyMap.urls')),
    url(r'^$', include('PsyMap.urls')),
)