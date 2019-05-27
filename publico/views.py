# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import utils
from django.views.generic import TemplateView

from tenant_schemas.utils import remove_www

from publico.models import ErpBrClient


class PublicHomeView(TemplateView):
    template_name = "publico/index.html"

    def get_context_data(self, **kwargs):
        context = super(PublicHomeView, self).get_context_data(**kwargs)

        hostname_without_port = remove_www(self.request.get_host().split(':')[0])

        try:
            ErpBrClient.objects.get(schema_name='public')
        except utils.DatabaseError:
            context['need_sync'] = True
            context['shared_apps'] = settings.SHARED_APPS
            context['tenants_list'] = []
            return context
        except ErpBrClient.DoesNotExist:
            context['no_public_tenant'] = True
            context['hostname'] = hostname_without_port

        if ErpBrClient.objects.count() == 1:
            context['only_public_tenant'] = True

        context['tenants_list'] = ErpBrClient.objects.all()
        return context
