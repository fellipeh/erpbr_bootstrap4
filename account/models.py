# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUser(AbstractUser):
    data_cadastro = models.DateTimeField(_('Data Cadastro'), default=timezone.now)
    user_loja = models.BooleanField(_('Usuário da Loja Virtual'), default=False)

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        if self.first_name or self.last_name:
            return self.get_full_name()
        return self.email

    def get_full_name(self):
        # Need these method to prevent django crash
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        # Need these method to prevent django crash
        return self.first_name

    def save(self, *args, **kwargs):

        # Atualizar datas criacao edicao
        if not self.data_cadastro:
            self.data_cadastro = timezone.now()
        return super(CustomUser, self).save(*args, **kwargs)

