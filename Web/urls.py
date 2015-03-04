from django.conf.urls import patterns, include, url
from django.contrib import admin

from PsyMap.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^PsyMap/', include('PsyMap.urls')),
)