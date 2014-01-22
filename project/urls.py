# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    (r'^', include('inei.planilla.urls')),
)

handler404 = 'home.views.get404page'
handler500 = 'home.views.get500page'

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$',
            serve, {'document_root': settings.STATIC_ROOT}),
        # url(r'^favicon\.ico$',
        #     'django.views.generic.simple.redirect_to',
        #     {'url': '/static/images/favicon.ico'}),
    )
