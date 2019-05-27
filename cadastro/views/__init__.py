# -*- coding: utf-8 -*-

from .cliente import cliente_list, cliente_create, cliente_delete, cliente_update
from .fornecedor import fornecedor_list, fornecedor_create, fornecedor_delete, fornecedor_update

__all__ = [
    'cliente_list', 'cliente_create', 'cliente_delete', 'cliente_update',
    'fornecedor_list', 'fornecedor_create', 'fornecedor_delete', 'fornecedor_update',
]
