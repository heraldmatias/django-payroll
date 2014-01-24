# -*- coding: utf-8 -*-
from twisted.scripts.trial import _initialDebugSetup
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
                    planilla['num_reg'] = reg
                    planilla['codi_empl_per'] = item.codi_empl_per
                    planilla['desc_plan_stp'] = item.desc_plan_stp
                    concepto = '%s_%s' % (item.codi_conc_tco, item.flag_folio)
                    planilla[concepto] = item.valo_calc_phi
                if len(data) == reg:
                    data.append(planilla)
            else:
                data = [dict() for r in range(folio.reg_folio)]
            formset = PlanillaHistoricasFormSet(initial=data, concepto=conceptos,
                                                prefix='cf')#queryset=planilla_historicas,
    return render_to_response('home/registros.html', {
        'tomo': tomo,
        'folio': folio,
        'conceptos': conceptos,
        'formset': formset,
    }, context_instance=RequestContext(request))


def set_registros(request):
    vtomo = request.POST.get('tomo', None)
    vfolio = request.POST.get('folio', None)
    folio = Folios.objects.get(num_folio=vfolio, codi_tomo=vtomo)
    conceptos = ConceptosFolios.objects.filter(codi_folio=folio).order_by('orden_conc_folio')
    formset = PlanillaHistoricasFormSet(request.POST, concepto=conceptos,
                                                prefix='cf')
    for form in formset:
        for f in form:
            print f.value()
        # sql =  'SELECT fn_planilla (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # periodo = folio.per_folio
        # empleado = data['codi_empl_per']
        # print empleado
        # $userid = $this->sc->getToken()->getUser()->getId();
        #     $conn->beginTransaction();
        #     $stmt = $conn->prepare(
        #             'SELECT fn_planilla (:aid, :aano_peri_tpe, :anume_peri_tpe,
        #                         :avalo_calc_phi, :atipo_plan_tpl, :asubt_plan_stp,
        #                         :acodi_empl_per, :acodi_conc_tco, :acodi_folio,
        #                         :adesc_plan_stp, :aflag_folio, :anum_reg,
        #                         :ausu_crea_id, :ausu_mod_id)'
        #     );
        #     $_periodo = $object->getPeriodoFolio();
        #     $periodo = strlen($_periodo)<2?
        #             str_pad($_periodo, 2, '0', STR_PAD_LEFT):
        #             strlen($_periodo)===2?$_periodo:'00';
        #     foreach ($data as $key1 => $planilla) {
        #         if ($key1 >= $object->getRegistrosFolio())
        #             break;
        #         $reg = $planilla['registro'];
        #         $dni = $planilla['codiEmplPer'];
        #         $descripcion = $planilla['descripcion'];
        #         $codigos = explode(',', $planilla['codigos']);
        #         unset($planilla['codiEmplPer']);
        #         unset($planilla['descripcion']);
        #         unset($planilla['registro']);
        #         unset($planilla['codigos']);
        #         $co = 0;
        #         foreach ($planilla as $key => $valor) {
        #             $pos = strpos($key, '_');
        #             $stmt->bindValue('aid', array_key_exists($co, $codigos) ?
        #                             is_numeric($codigos[$co]) ? $codigos[$co] : null : null);
        #             $stmt->bindValue('aano_peri_tpe', $object->getTomo()->getAnoTomo());
        #             $stmt->bindValue('anume_peri_tpe', $periodo);
        #             $stmt->bindValue('avalo_calc_phi', $valor);
        #             $stmt->bindValue('atipo_plan_tpl', is_object($object->getTipoPlanTpl()) ? $object->getTipoPlanTpl()->getTipoPlanTpl() : $object->getTipoPlanTpl());
        #             $stmt->bindValue('asubt_plan_stp', $object->getSubtPlanStp());
        #             $stmt->bindValue('acodi_empl_per', $dni);
        #             $stmt->bindValue('acodi_conc_tco', substr($key, 0, $pos));
        #             $stmt->bindValue('acodi_folio', $object->getCodiFolio());
        #             $stmt->bindValue('adesc_plan_stp', $descripcion);
        #             $stmt->bindValue('aflag_folio', substr($key, $pos + 1));
        #             $stmt->bindValue('anum_reg', $reg);
        #             $stmt->bindValue('ausu_crea_id', $userid);
        #             $stmt->bindValue('ausu_mod_id', $userid);
        #             $stmt->execute();
        #             $codigos[$co] = -1;
        #             $co++;
        #         }
        #         /*                 * ***************ELIMINAMOS LAS FILAS QUE YA NO
        #          * SE ENCUENTREN EN LA MATRIZ******************* */
        #         $q = $this->em->createQuery('delete from
        #             IneiPayrollBundle:PlanillaHistoricas m where m.id in (:ids)');
        #         $q->setParameter('ids', $codigos);
        #         $q->execute();
        #     }

    return render_to_response('home/registros.html', {
        'conceptos': conceptos,
        'formset': formset,
    }, context_instance=RequestContext(request))
