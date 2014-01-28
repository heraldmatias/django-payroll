# -*- coding: utf-8 -*-
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from models import Tomos, Folios, ConceptosFolios, PlanillaHistoricas
from forms import PlanillaHistoricasFormSet
from django.db import connection, transaction
from simplejson import dumps


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
                html += '<option value="' + str(folio.num_folio) + '">' + str(folio.num_folio) + '</option>'
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
            conceptos = ConceptosFolios.objects.filter(codi_folio=folio).order_by('orden_conc_folio')
            planilla_historicas = PlanillaHistoricas.objects.filter(codi_folio=folio.codi_folio).order_by('num_reg')
            if planilla_historicas.exists():
                data = []
                codigos = []
                reg = planilla_historicas[0].num_reg
                planilla = {}
                for item in planilla_historicas:
                    if reg == item.num_reg:
                        reg = item.num_reg
                        codigos.append(str(item.id))
                        planilla['num_reg'] = reg
                        planilla['codi_empl_per'] = item.codi_empl_per
                        planilla['desc_plan_stp'] = item.desc_plan_stp
                        concepto = '%s_%s' % (item.codi_conc_tco, item.flag_folio)
                        planilla[concepto] = item.valo_calc_phi
                        continue
                    reg = item.num_reg
                    planilla['codigos'] = ','.join(codigos)
                    data.append(planilla)
                    planilla = {}
                    codigos = []
                    codigos.append(str(item.id))
                    planilla['num_reg'] = reg
                    planilla['codi_empl_per'] = item.codi_empl_per
                    planilla['desc_plan_stp'] = item.desc_plan_stp
                    concepto = '%s_%s' % (item.codi_conc_tco, item.flag_folio)
                    planilla[concepto] = item.valo_calc_phi
                if len(data) == reg:
                    planilla['codigos'] = ','.join(codigos)
                    data.append(planilla)
            else:
                if folio.reg_folio:
                    data = [dict() for r in range(folio.reg_folio)]
                else:
                    data = []
            formset = PlanillaHistoricasFormSet(initial=data, concepto=conceptos,
                                                prefix='cf')#queryset=planilla_historicas,
    return render_to_response('home/registros.html', {
        'tomo': tomo,
        'folio': folio,
        'conceptos': conceptos,
        'formset': formset,
    }, context_instance=RequestContext(request))

@transaction.atomic
def set_registros(request):
    vtomo = request.POST.get('tomo', None)
    vfolio = request.POST.get('folio', None)
    folio = Folios.objects.get(num_folio=vfolio, codi_tomo=vtomo)
    conceptos = ConceptosFolios.objects.filter(codi_folio=folio).order_by('orden_conc_folio')
    formset = PlanillaHistoricasFormSet(request.POST, concepto=conceptos,
                                                prefix='cf')
    conceptos = []
    ncodigos = 0
    cursor = connection.cursor()

    for fila, form in enumerate(formset):
        for f in form:
            if f.name.startswith('C'):
                concepto = f.name.split('_')
                conceptos.append((concepto[0], concepto[1], f.value()))
            elif f.name == 'codi_empl_per':
                empleado = f.value()
            elif f.name == 'desc_plan_stp':
                descripcion = f.value()
            elif f.name == 'codigos':
                codigos = f.value()
        try:
            codigos = codigos.split(',')
            ncodigos = len(codigos)-1
        except:
            codigos = []
        #print 'NUMERO DE REGISTRO = %s' % fila
        for i, concepto in enumerate(conceptos):
            # print 'SELECT fn_planilla (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' % (codigos[i] if i <= ncodigos else None,
            #     folio.codi_tomo.ano_tomo, folio.per_folio, concepto[2], folio.tipo_plan_tpl,
            #     folio.subt_plan_stp, empleado, concepto[0], folio.codi_folio, descripcion,
            #     concepto[1], fila, request.user.id, request.user.id)
            cursor.execute('SELECT fn_planilla (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                codigos[i] if i <= ncodigos != 0 else None,
                folio.codi_tomo.ano_tomo, folio.per_folio, concepto[2], folio.tipo_plan_tpl,
                folio.subt_plan_stp, empleado, concepto[0], folio.codi_folio, descripcion,
                concepto[1], fila, request.user.id, request.user.id))
        conceptos = []

    response = HttpResponse(content=dumps({
        'data': (int(vfolio)+1),
        'success': True,
        'error': None}), content_type='application/json')
    return response

    # return render_to_response('home/registros.html', {
    #     'conceptos': conceptos,
    #     'formset': formset,
    # }, context_instance=RequestContext(request))
