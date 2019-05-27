# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from cadastro.models import Cliente
from cadastro.forms import ClienteForm

import django_filters
from erpbr.mixins import ERPbrViewMixin, FilterMixin


class ClienteFilter(django_filters.FilterSet):
    razao_social = django_filters.CharFilter(lookup_expr='iexact')
    email = django_filters.CharFilter(lookup_expr='iexact')
    fis_cpf = django_filters.CharFilter(lookup_expr='iexact')
    jur_cnpj = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Cliente
        fields = ['razao_social', 'email', 'fis_cpf', 'jur_cnpj']


class ClienteView(ERPbrViewMixin, FilterMixin, ListView):
    http_mothod_names = ['get']
    template_name = 'cadastro/cliente/list.html'
    model = Cliente
    paginate_by = 20
    filter_class = ClienteFilter


cliente_list = login_required(ClienteView.as_view())


class ClienteCreateView(ERPbrViewMixin, CreateView):
    template_name = 'cadastro/cliente/form.html'
    model = Cliente
    form_class = ClienteForm

    def get_success_url(self):
        return reverse('cadastro:cliente_list')

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['criado_por'] = self.logged_user.pk
        return super(ClienteCreateView, self).post(request, *args,
                                                   **kwargs)

    def get_form(self, form_class=None):
        form = super(ClienteCreateView, self).get_form(form_class)
        # form.fields["datasets"].queryset = Dataset.objects.filter(
        #     users=self.request.user)
        return form

    def get_form_kwargs(self):
        kwargs = super(ClienteCreateView, self).get_form_kwargs()
        kwargs['logged_user'] = self.logged_user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs = super(ClienteCreateView, self).get_context_data()
        return kwargs


cliente_create = login_required(ClienteCreateView.as_view())


class ClienteUpdateView(ERPbrViewMixin, UpdateView):
    template_name = 'cadastro/cliente/form.html'
    model = Cliente
    form_class = ClienteForm

    def get_success_url(self):
        return reverse('cadastro:cliente_list')

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['user_updated'] = self.logged_user.pk
        return super(ClienteUpdateView, self).post(request, *args,
                                                   **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ClienteUpdateView, self).get_form_kwargs()
        kwargs['logged_user'] = self.logged_user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs = super(ClienteUpdateView, self).get_context_data()
        return kwargs


cliente_update = login_required(ClienteUpdateView.as_view())


class ClienteDelete(DeleteView):
    template_name = 'cadastro/cliente/delete_confirm.html'
    model = Cliente
    pk_url_kwarg = 'cliente_id'

    def get_success_url(self):
        return reverse('core:cliente_list')


cliente_delete = login_required(ClienteDelete.as_view())
