# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello_world/$',hello_world),
    url(r'^$', 'article.views.home'),
    url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^test/$', 'article.views.test'),
)
