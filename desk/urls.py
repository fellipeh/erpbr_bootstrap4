# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from desk import views

app_name = 'desk'

urlpatterns = [
    url(r'^$', views.dashboard_view, name='dashboard'),

]
