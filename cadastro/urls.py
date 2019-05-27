# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from cadastro import views

app_name = 'cadastro'

urlpatterns = [
    url(r'^clientes$', views.cliente_list, name='cliente_list'),
    url(r'^clientes/(?P<pk>\d+)$', views.cliente_update, name='cliente_update'),
    url(r'^clientes/new$', views.cliente_create, name='cliente_create'),
    url(r'^clientes/delete/(?P<cliente_id>\d+)$', views.cliente_delete, name='cliente_delete'),

    url(r'^fornecedor$', views.fornecedor_list, name='fornecedor_list'),
    url(r'^fornecedor/(?P<pk>\d+)$', views.fornecedor_update, name='fornecedor_update'),
    url(r'^fornecedor/new$', views.fornecedor_create, name='fornecedor_create'),
    url(r'^fornecedor/delete/(?P<fornecedor_id>\d+)$', views.fornecedor_delete, name='fornecedor_delete'),

]
