# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import HiddenInput
from cadastro.models import (Cliente, Fornecedor)


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.logged_user = kwargs.pop('logged_user', None)
        super(ClienteForm, self).__init__(*args, **kwargs)
        # self.fields['tipo_pessoa'].widget.attrs.update({'class': 'selectpicker'})
        self.fields['tipo_pessoa'].widget.attrs['ng-model'] = 'form.tipo_pessoa'

    def clean(self):
        cleaned_data = super(ClienteForm, self).clean()
        cleaned_data['criado_por'] = self.logged_user
        return cleaned_data

    class Meta:
        model = Cliente
        fields = '__all__'
        # widgets = {
        #     'criado_por': HiddenInput(),
        # }


class FornecedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.logged_user = kwargs.pop('logged_user', None)
        super(FornecedorForm, self).__init__(*args, **kwargs)
        # self.fields['tipo_pessoa'].widget.attrs.update({'class': 'selectpicker'})
        self.fields['tipo_pessoa'].widget.attrs['ng-model'] = 'form.tipo_pessoa'

    def clean(self):
        cleaned_data = super(FornecedorForm, self).clean()
        cleaned_data['criado_por'] = self.logged_user
        return cleaned_data

    class Meta:
        model = Fornecedor
        fields = '__all__'
        # widgets = {
        #     'criado_por': HiddenInput(),
        # }
