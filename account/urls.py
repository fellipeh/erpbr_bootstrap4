# -*- coding: utf-8 -*-
from django.conf.urls import url

from account import views

app_name = 'account'

urlpatterns = [
    url(r'^login/$', views.AccountLogin.as_view(), name='erpbr_login'),
    url(r'^logout/$', views.account_logout, name='erpbr_logout'),
]
