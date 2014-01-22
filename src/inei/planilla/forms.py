from django.forms.models import BaseModelFormSet
from django.forms.models import modelformset_factory
from django import forms
from models import PlanillaHistoricas, ConceptosFolios, Folios, Tomos

class PlanillaHistoricasForm(forms.ModelForm):

    def __init__(self, concepto, *args, **kwargs):
        super(PlanillaHistoricasForm, self).__init__(*args, **kwargs)
        for conc in concepto:
            self.fields['prueba'] = forms.CharField()

    class Meta:
        model = PlanillaHistoricas

class BasePlanillaHistoricasFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        self.concepto = kwargs['concepto']
        del kwargs['concepto']
        super(BasePlanillaHistoricasFormSet, self).__init__(*args, **kwargs)

    def _construct_form(self, i, **kwargs):
        kwargs['concepto'] = self.concepto
        return super(BasePlanillaHistoricasFormSet, self)._construct_form(i, **kwargs)

    def add_fields(self, form, index):
        super(BasePlanillaHistoricasFormSet, self).add_fields(form, index)

PlanillaHistoricasFormSet = modelformset_factory(PlanillaHistoricas, form=PlanillaHistoricasForm,
                                       formset=BasePlanillaHistoricasFormSet,
                                       extra=0, exclude=('id', ), can_delete=False)