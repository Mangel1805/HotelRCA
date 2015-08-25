from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************Ingreso*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarIngreso.as_view(),name='crearIngreso'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarIngreso.as_view(),name='editarIngreso'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarIngreso.as_view(),name='eliminarIngreso'),
    url(r'^listar/$', listarIngreso.as_view(),name='listarIngreso'),
    url(r'^buscar/$', buscarIngreso.as_view(),name='buscarIngreso'),
    url(r'^generar_pdf/$','apps.ingresos.views.generar_pdf', name='pdf_Ingresos'),
)