from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', index.as_view(),name='home'),
    #********************Egreso*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarEgreso.as_view(),name='crearEgreso'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarEgreso.as_view(),name='editarEgreso'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarEgreso.as_view(),name='eliminarEgreso'),
    url(r'^listar/$', listarEgreso.as_view(),name='listarEgreso'),
    url(r'^buscar/$', buscarEgreso.as_view(),name='buscarEgreso'),
    url(r'^generar_pdf/$','apps.egresos.views.generar_pdf', name='pdf_Egresos'),
)