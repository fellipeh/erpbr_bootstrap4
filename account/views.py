# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.views import logout_then_login

from account.forms import LoginForm


class AccountLogin(View):
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': LoginForm()})

    @staticmethod
    def authenticate_user(form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        return authenticate(username=username, password=password)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = self.authenticate_user(form)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    error_msg = _("Usuário Inativo. Por favor, entre em contato com um Administrador.")

            else:
                error_msg = _("Usuário/Senha incorretos. Por favor, tente novamente.")
            form.add_error(None, error_msg)

        return render(request, self.template_name, {'form': form})


def account_logout(request):
    return logout_then_login(request)
