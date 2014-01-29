# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('inei.planilla.views',
       url(r'^$', 'get_login', name='planillas-login'),
       url(r'^registrar-planilla/$', 'get_registrar_planilla', name='planillas-registrar-planilla'),
       url(r'^get_folios/$', 'get_folios', name='planillas-get_folios'),
       url(r'^get_registros/$', 'get_registros', name='planillas-get-registros'),
       url(r'^set_registros/$', 'set_registros', name='planillas-set-registros'),
       url(r'^autosave/$', 'autoguardado', name='planillas-autosave-registros'),
)