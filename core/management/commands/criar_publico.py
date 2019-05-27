# -*- coding: utf-8 -*-

from datetime import date
from django.core.management.base import BaseCommand
from django.conf import settings

from publico.models import ErpBrClient


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Criando área Publica...')

        # create your public tenant
        tenant = ErpBrClient(domain_url=options['domain'],
                             # don't add your port or www here! on a local server you'll want to use localhost here
                             schema_name='public',
                             nome=options['nome'],
                             documento='0',
                             paid_until=date.today(),
                             on_trial=False)

        tenant.auto_create_schema = True
        tenant.save()

        print('Criando Public Tenant... OK')

    def add_arguments(self, parser):
        parser.add_argument('domain', type=str)
        parser.add_argument('nome', type=str)
