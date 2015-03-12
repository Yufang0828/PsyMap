from django.conf.urls import patterns, include, url
# from django.contrib import admin

from PsyMap.views import *

urlpatterns = patterns(
    '',
    url(r'^PsyMap/', include('PsyMap.urls')),
)