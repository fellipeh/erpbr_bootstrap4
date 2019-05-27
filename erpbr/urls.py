from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url, include
from django.views.static import serve

urlpatterns = []

if settings.DEBUG:
    urlpatterns.extend([
        url(
            r'^media/(?P<path>.*)$',
            serve,
            {'document_root': settings.MEDIA_ROOT}
        )
    ])

urlpatterns.extend([
    path('desk/admin/', admin.site.urls),
    # path(r'^accounts/manager/', include('password_reset.urls')),
    url(r'^desk/account/', include('account.urls', namespace='account')),
    url(r'^desk/cadastro/', include('cadastro.urls', namespace='cadastro')),
    # url(r'^desk/financeiro/', include('financeiro.urls', namespace='financeiro')),
    # url(r'^desk/estoque/', include('estoque.urls', namespace='estoque')),
    #
    # url(r'^desk/api/v1/', include('api.urls', namespace='api')),
    url(r'^desk/', include('desk.urls', namespace='desk')),

    url(r'^', include('core.urls', namespace='core')),
])

admin.site.site_header = _('Administração do ERPbr')
admin.site.site_title = _('Administração do ERPbr')
admin.site.index_title = ""
# admin.site.unregister(Group)
