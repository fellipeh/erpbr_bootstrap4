# -*- encoding: utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('form/default_field.html')
def default_field(field, hint=None):
    if hint is None:
        hint = field.help_text
    return {'field': field, 'hint': hint}


@register.filter('is_file_widget')
def is_file_widget(field):
    return 'FileInput' in field.field.widget.__class__.__name__
