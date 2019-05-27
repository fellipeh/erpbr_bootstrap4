# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models
from tenant_schemas.models import TenantMixin


class ErpBrClient(TenantMixin):
    created_on = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    email = models.EmailField()
    on_trial = models.BooleanField(default=False)
    trial_finish = models.DateField(null=True, blank=True)
    paid_until = models.DateField(null=True, blank=True)
    google_analytics = models.CharField(max_length=50, null=True, blank=True, default='UA-49883581-3')
    mensagem = models.TextField(null=True, blank=True)
    exibiu_msg = models.BooleanField(default=False)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
