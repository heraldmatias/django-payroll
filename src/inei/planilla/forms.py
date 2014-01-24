from django.forms.formsets import BaseFormSet, formset_factory
from django.forms.models import BaseModelFormSet
from django.forms.models import modelformset_factory
from django import forms
from models import PlanillaHistoricas, ConceptosFolios, Folios, Tomos


class PlanillaHistoricasForm(forms.Form):
    codi_empl_per = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'nombre', 'placeholder': 'Apellidos y Nombres'}))
    desc_plan_stp = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': 1}))

    def __init__(self, concepto, *args, **kwargs):
        super(PlanillaHistoricasForm, self).__init__(*args, **kwargs)
        campos = dict()
        for conc in concepto:
            codigo = conc.codi_conc_tco.codi_conc_tco
            descripcion = conc.codi_conc_tco.desc_cort_tco
            tipo = conc.codi_conc_tco.tipo_conc_tco
            clase = 'remuneraciones' if codigo == 'C373' else 'descuentos' if codigo == 'C374' else 'total' if codigo == 'C12' else 'monto'
            attrs = {
                'class': clase,
                'data-title': descripcion,
                'data-tipo': tipo,
                'style': 'width:auto;font-size:15px;',
                'maxlength': 35,
                'placeholder': descripcion
            }
            if codigo in campos:
                campos[codigo] += 1
            else:
                campos[codigo] = 1
            index = campos[codigo]
            flag = '_%s' % index
            self.fields['%s%s' % (codigo, flag)] = forms.CharField(widget=forms.TextInput(attrs=attrs))
        self.fields['codigos'] = forms.CharField(max_length=700, widget=forms.HiddenInput())


class BasePlanillaHistoricasFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        self.concepto = kwargs['concepto']
        del kwargs['concepto']
        super(BasePlanillaHistoricasFormSet, self).__init__(*args, **kwargs)

    def _construct_form(self, i, **kwargs):
        kwargs['concepto'] = self.concepto
        return super(BasePlanillaHistoricasFormSet, self)._construct_form(i, **kwargs)

    def add_fields(self, form, index):
        super(BasePlanillaHistoricasFormSet, self).add_fields(form, index)


PlanillaHistoricasFormSet = formset_factory(#form=PlanillaHistoricasForm,
                                            form=PlanillaHistoricasForm,
                                            formset=BasePlanillaHistoricasFormSet,
                                            extra=0, can_delete=False) #exclude=('id', ))