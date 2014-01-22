# -*- coding: utf-8 -*-
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from models import Tomos, Folios, ConceptosFolios, PlanillaHistoricas
from forms import PlanillaHistoricasFormSet

def get_login(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':

            usuario = request.POST.get('usuario', None)
            contrasena = request.POST.get('contrasena', None)

            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return render_to_response('home/index.html', {}, context_instance=RequestContext(request))

        return render_to_response('home/login.html', {}, context_instance=RequestContext(request))
    else:
        return render_to_response('home/index.html', {}, context_instance=RequestContext(request))

def get_registrar_planilla(request):

    tomos = Tomos.objects.all().order_by('codi_tomo')

    return render_to_response('home/registrar_planilla.html', {
        'tomos': tomos,
    }, context_instance=RequestContext(request))


def get_folios(request):
    html = ''
    if request.method == 'POST':
        tomo = request.POST.get('tomo', None)
        if tomo and Tomos.objects.filter(codi_tomo=tomo).exists():
            folios = Folios.objects.filter(codi_tomo=tomo).order_by('num_folio')
            for folio in folios:
                html+='<option value="'+str(folio.num_folio)+'">'+str(folio.num_folio)+'</option>'
    return HttpResponse(html)


def get_registros(request):
    tomo = None
    folio = None
    conceptos = None
    if request.method == 'POST':
        vtomo = request.POST.get('tomo', None)
        vfolio = request.POST.get('folio', None)
        if vtomo and vfolio and Folios.objects.filter(codi_tomo=vtomo, num_folio=vfolio).exists():
            tomo = Tomos.objects.get(codi_tomo=vtomo)
            folio = Folios.objects.get(num_folio=vfolio, codi_tomo=vtomo)
            conceptos = ConceptosFolios.objects.filter(codi_folio=folio)
            planilla_historicas = PlanillaHistoricas.objects.filter(codi_folio=folio.codi_folio)
            formset = PlanillaHistoricasFormSet(queryset=planilla_historicas, concepto=conceptos, prefix='cf')
    return render_to_response('home/registros.html', {
        'tomo': tomo,
        'folio': folio,
        'conceptos': conceptos,
        'formset': formset,
    }, context_instance=RequestContext(request))