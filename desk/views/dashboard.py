# -*- encoding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'desk/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        # context['total_clientes'] = Cliente.objects.all().count()
        # context['total_clientes_ontem'] = Cliente.objects.filter(
        #     data_criacao__gte=datetime.date.today() - datetime.timedelta(days=1)).count()

        return context


dashboard_view = login_required(DashboardView.as_view())
