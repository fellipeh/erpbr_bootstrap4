# -*- encoding: utf-8 -*-
from django import template
from django.urls import reverse as r


register = template.Library()


@register.simple_tag
def navactive(request, urls):
    if request.path in (r(url) for url in urls.split()):
        return "active"
    return ""
