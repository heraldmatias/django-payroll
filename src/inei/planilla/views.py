# -*- coding: utf-8 -*-
import locale

from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout

def get_login(request):

    if request.POST:

        usuario = request.POST.get('usuario', None)
        contrasena = request.POST.get('contrasena', None)

        user = authenticate(username=usuario, password=contrasena)

        if user is not None:
            login(request, user)
            return render_to_response('home/index.html', {}, context_instance=RequestContext(request))
    #elif request.user.is_authenticated:
    #    return render_to_response('home/index.html', {}, context_instance=RequestContext(request))

    return render_to_response('home/login.html', {}, context_instance=RequestContext(request))