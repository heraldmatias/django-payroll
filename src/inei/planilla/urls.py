# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('inei.planilla.views',
       url(r'^$', 'get_login', name='planillas-login'),
)