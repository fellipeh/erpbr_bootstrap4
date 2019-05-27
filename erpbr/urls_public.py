from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import Group

from publico.views import PublicHomeView


urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', PublicHomeView.as_view()),
]


admin.site.site_header = 'Administração do ERPbr'
admin.site.site_title = 'Administração do ERPbr'
admin.site.index_title = ""
# admin.site.unregister(Group)