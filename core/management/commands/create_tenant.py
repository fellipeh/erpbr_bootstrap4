import sys
import time
from django.core.management.base import BaseCommand
from django.conf import settings

from publico.models import ErpBrClient


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Criando Tenant...')

        # create your public tenant
        tenant = ErpBrClient(domain_url=options['domain'],
                             # don't add your port or www here! on a local server you'll want to use localhost here
                             schema_name=options['schema'],
                             nome=options['nome'],
                             documento=options['doc'],
                             paid_until='2016-12-05',
                             on_trial=False)

        tenant.save()

        print('Criando Tenant... OK')

    def add_arguments(self, parser):
        parser.add_argument('domain', type=str)
        parser.add_argument('schema', type=str)
        parser.add_argument('nome', type=str)
        parser.add_argument('doc', type=str)
