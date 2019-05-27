# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from cadastro.models import Fornecedor
from cadastro.forms import FornecedorForm

import django_filters
from erpbr.mixins import ERPbrViewMixin, FilterMixin


class FornecedorFilter(django_filters.FilterSet):
    razao_social = django_filters.CharFilter(lookup_expr='iexact')
    email = django_filters.CharFilter(lookup_expr='iexact')
    fis_cpf = django_filters.CharFilter(lookup_expr='iexact')
    jur_cnpj = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Fornecedor
        fields = ['razao_social', 'email', 'fis_cpf', 'jur_cnpj']


class FornecedorView(ERPbrViewMixin, FilterMixin, ListView):
    http_mothod_names = ['get']
    template_name = 'cadastro/fornecedor/list.html'
    model = Fornecedor
    paginate_by = 20
    filter_class = FornecedorFilter


fornecedor_list = login_required(FornecedorView.as_view())


class FornecedorCreateView(ERPbrViewMixin, CreateView):
    template_name = 'cadastro/fornecedor/form.html'
    model = Fornecedor
    form_class = FornecedorForm

    def get_success_url(self):
        return reverse('cadastro:fornecedor_list')

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['criado_por'] = self.logged_user.pk
        return super(FornecedorCreateView, self).post(request, *args,
                                                   **kwargs)

    def get_form(self, form_class=None):
        form = super(FornecedorCreateView, self).get_form(form_class)
        # form.fields["datasets"].queryset = Dataset.objects.filter(
        #     users=self.request.user)
        return form

    def get_form_kwargs(self):
        kwargs = super(FornecedorCreateView, self).get_form_kwargs()
        kwargs['logged_user'] = self.logged_user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs = super(FornecedorCreateView, self).get_context_data()
        return kwargs


fornecedor_create = login_required(FornecedorCreateView.as_view())


class FornecedorUpdateView(ERPbrViewMixin, UpdateView):
    template_name = 'cadastro/fornecedor/form.html'
    model = Fornecedor
    form_class = FornecedorForm

    def get_success_url(self):
        return reverse('cadastro:fornecedor_list')

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['user_updated'] = self.logged_user.pk
        return super(FornecedorUpdateView, self).post(request, *args,
                                                   **kwargs)

    def get_form_kwargs(self):
        kwargs = super(FornecedorUpdateView, self).get_form_kwargs()
        kwargs['logged_user'] = self.logged_user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs = super(FornecedorUpdateView, self).get_context_data()
        return kwargs


fornecedor_update = login_required(FornecedorUpdateView.as_view())


class FornecedorDelete(DeleteView):
    template_name = 'cadastro/fornecedor/delete_confirm.html'
    model = Fornecedor
    pk_url_kwarg = 'fornecedor_id'

    def get_success_url(self):
        return reverse('core:fornecedor_list')


fornecedor_delete = login_required(FornecedorDelete.as_view())
