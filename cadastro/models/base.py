# -*- coding: utf-8 -*-
from django_tools.middlewares import ThreadLocal

from django.utils.translation import ugettext_lazy as _
import re

from django.db import models
from django.utils import timezone

from .bancos import BANCOS
from account.models import CustomUser
from erpbr.choices import *


class PessoaBase(models.Model):
    criado_por = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='PessoaCriadoPor')
    data_criacao = models.DateTimeField(_('Dt/Hr Criação'), editable=False)
    data_edicao = models.DateTimeField(_('Dt/Hr Edição'), editable=False)
    editado_por = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='PessoaEditadoPor')

    # Dados
    razao_social = models.CharField(_('Razão Social/Nome'), max_length=255)
    inscricao_municipal = models.CharField(_('Insc. Municipal'), max_length=32, null=True, blank=True)
    tipo_pessoa = models.CharField(_('Tipo Pessoa'), max_length=2, choices=TIPO_PESSOA, default='PF')
    informacoes_adicionais = models.TextField(_('Inf. Adicionais'), null=True, blank=True)

    # Endereço
    tipo_endereco = models.CharField(_('Tipo Endereço'), max_length=3, null=True, blank=True, choices=TIPO_ENDERECO)
    logradouro = models.CharField(_('Logradouro'), max_length=255, null=True, blank=True)
    numero = models.CharField(_('Num.'), max_length=16, null=True, blank=True)
    bairro = models.CharField(_('Bairro'), max_length=64, null=True, blank=True)
    complemento = models.CharField(_('Compl'), max_length=64, null=True, blank=True)
    pais = models.CharField(_('País'), max_length=32, null=True, blank=True, default='Brasil')
    cpais = models.CharField(_('Código País'), max_length=5, null=True, blank=True, default='1058')
    municipio = models.CharField(_('Município'), max_length=64, null=True, blank=True)
    cmun = models.CharField(_('Cód. Município'), max_length=9, null=True, blank=True)
    cep = models.CharField(_('CEP'), max_length=16, null=True, blank=True)
    uf = models.CharField(_('UF'), max_length=3, null=True, blank=True, choices=UF_SIGLA)

    # Telefones
    tel1 = models.CharField(_('Telefone 1'), max_length=32, null=True, blank=True)
    tel1_tipo = models.CharField(_('Tipo'), max_length=8, choices=TIPO_TELEFONE, null=True, blank=True)
    tel2 = models.CharField(_('Telefone 2'), max_length=32, null=True, blank=True)
    tel2_tipo = models.CharField(_('Tipo'), max_length=8, choices=TIPO_TELEFONE, null=True, blank=True)
    tel3 = models.CharField(_('Telefone 3'), max_length=32, null=True, blank=True)
    tel4_tipo = models.CharField(_('Tipo'), max_length=8, choices=TIPO_TELEFONE, null=True, blank=True)

    site = models.URLField(verbose_name=_('Site'), max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name=_('E-Mail'), max_length=255, null=True, blank=True)

    banco_padrao = models.CharField(_('Banco Padrão'), max_length=3, null=True, blank=True, choices=BANCOS)
    banco_agencia = models.CharField(_('Agência'), max_length=30, null=True, blank=True)
    banco_agencia_dig = models.CharField(_('Díg'), max_length=3, null=True, blank=True)
    banco_conta = models.CharField(_('Conta'), max_length=30, null=True, blank=True)
    banco_conta_dig = models.CharField(_('Díg'), max_length=3, null=True, blank=True)

    # Dados Pessoa Física
    fis_cpf = models.CharField(_('CPF'), max_length=32, null=True, blank=True)
    fis_rg = models.CharField(_('RG'), max_length=32, null=True, blank=True)
    fis_dtnasc = models.DateField(_('Data Nasc.'), null=True, blank=True)

    # Dados Pessoa Juridica
    jur_cnpj = models.CharField(_('CNPJ'), max_length=32, null=True, blank=True)
    jur_nome_fantasia = models.CharField(_('Nome Fantasia'), max_length=255, null=True, blank=True)
    jur_inscricao_estadual = models.CharField(_('Insc. Estadual'), max_length=32, null=True, blank=True)
    jur_responsavel = models.CharField(_('Responsável'), max_length=32, null=True, blank=True)
    jur_sit_fiscal = models.CharField(_('Enquad. Fiscal'), max_length=2, null=True, blank=True,
                                      choices=ENQUADRAMENTO_FISCAL)
    jur_suframa = models.CharField(_('SUFRAMA'), max_length=16, null=True, blank=True)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nome_razao_social = None

    def save(self, *args, **kwargs):
        # Atualizar datas criacao edicao
        user = ThreadLocal.get_current_user()

        self.criado_por = user
        if not self.data_criacao:
            self.data_criacao = timezone.now()
        self.data_edicao = timezone.now()
        return super(PessoaBase, self).save(*args, **kwargs)

    @property
    def format_endereco(self):
        return '{0}, {1} - {2}'.format(self.logradouro, self.numero, self.bairro)

    @property
    def format_endereco_completo(self):
        return '{0} - {1} - {2} - {3} - {4} - {5} - {6}'.format(self.logradouro, self.numero, self.bairro,
                                                                self.municipio, self.cep, self.uf, self.pais)

    @property
    def format_cpf(self):
        if self.fis_cpf:
            return 'CPF: {}'.format(self.fis_cpf)
        else:
            return ''

    @property
    def format_rg(self):
        if self.fis_rg:
            return 'RG: {}'.format(self.fis_rg)
        else:
            return ''

    @property
    def doc_apenas_digitos(self):
        if self.tipo_pessoa == 'PF':
            if self.fis_cpf:
                return re.sub('[./-]', '', self.fis_cpf)

        elif self.tipo_pessoa == 'PJ':
            if self.jur_cnpj:
                return re.sub('[./-]', '', self.jur_cnpj)

        else:
            return ''

    @property
    def inscricao_estadual(self):
        if self.tipo_pessoa == 'PF':
            return 'ISENTO'
        elif self.tipo_pessoa == 'PJ':
            if self.jur_inscricao_estadual:
                return re.sub('[./-]', '', self.jur_inscricao_estadual)
        else:
            return ''

    @property
    def uf_padrao(self):
        if self.uf:
            return self.uf
        else:
            return ''

    @property
    def format_cnpj(self):
        if self.jur_cnpj:
            return 'CNPJ: {}'.format(self.jur_cnpj)
        else:
            return ''

    @property
    def format_ie(self):
        if self.inscricao_estadual:
            return 'IE: {}'.format(self.inscricao_estadual)
        else:
            return ''

    def __unicode__(self):
        s = u'%s' % self.razao_social
        return s

    def __str__(self):
        s = u'%s' % self.razao_social
        return s
