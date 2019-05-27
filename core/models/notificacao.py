# -*- coding: utf-8 -*-
from django_tools.middlewares import ThreadLocal

from django.utils.translation import ugettext_lazy as _
import re

from django.db import models
from django.utils import timezone

from account.models import CustomUser


class Notificacao(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dthr_cadastro = models.DateTimeField(_('Data/Hora Cadastro'), default=timezone.now)
    texto = models.CharField(_('Mensagem'), max_length=255)
    lido = models.BooleanField(_('Lido'), default=False)
    notify_url = models.CharField(_('URL'), max_length=255, null=True, blank=True)
    notify_icon = models.CharField(_('Icon'), max_length=255, null=True, blank=True)
