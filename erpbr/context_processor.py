# -*- coding: utf-8 -*-
from erpbr.settings import PROJECT_VERSION, DEBUG

from core.models import Notificacao


def default_proc(request):
    notifications = Notificacao.objects.filter(usuario=request.user).filter(lido=False)
    return {
        'notificacoes': notifications,
        'project_version': PROJECT_VERSION,
        'debug': DEBUG
    }
