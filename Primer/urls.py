from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^sectoresbd/$', views.sectores, name='sectoressbd'),
    url(r'^confe/$', views.mencionar, name='mencionar'),
    url(r'^confe_tipo/$', views.prueba, name='prueba'),
]
