# -*- coding: utf-8 -*-
from django.db import models
from account.models import CustomUser
from .base import PessoaBase


class Fornecedor(PessoaBase):
    criado_por = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='FornecedorCriadoPor')
    editado_por = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='FornecedorEditadoPor')

    permissions = (
        ('view_content', 'Visualizar conteúdo'),
    )

    def __unicode__(self):
        s = u'%s' % self.razao_social
        return s

    def __str__(self):
        s = u'%s' % self.razao_social
        return s

    def __repr__(self):
        s = u'Fornecedor: %s' % self.razao_social
        return s
