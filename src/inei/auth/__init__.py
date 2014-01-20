from django.db.models import CharField
from inei.auth import validators

__author__ = 'holivares'

# TODO: Maybe move this into contrib, because it's specialized.


class CommaSeparatedStrField(CharField):
    default_validators = [validators.validate_comma_separated_str_list]
    description = "Comma-separated integers"

    def formfield(self, **kwargs):
        defaults = {
            'error_messages': {
                'invalid': u'Ingrese los proyectos separados por comas.',
            }
        }
        defaults.update(kwargs)
        return super(CommaSeparatedStrField, self).formfield(**defaults)


from django.forms.forms import BoundField

def add_control_label(f):
    def control_label_tag(self, contents=None, attrs=None):
        if attrs is None: attrs = {}
        attrs['class'] = 'control-label'
        return f(self, contents, attrs)
    return control_label_tag

BoundField.label_tag = add_control_label(BoundField.label_tag)