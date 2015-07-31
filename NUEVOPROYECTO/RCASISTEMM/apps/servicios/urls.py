from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************Servicio*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarServicio.as_view(),name='crearServicio'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarServicio.as_view(),name='editarServicio'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarServicio.as_view(),name='eliminarServicio'),
    url(r'^listar/$', listarServicio.as_view(),name='listarServicio'),
)