# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from core import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.home_view, name='homeview'),

]
