from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************Ciudad*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarCiudad.as_view(),name='crearCiudad'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarCiudad.as_view(),name='editarCiudad'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarCiudad.as_view(),name='eliminarCiudad'),
    url(r'^listar/$', listarCiudad.as_view(),name='listarCiudad'),
    url(r'^generar_pdf/$','apps.ciudad.views.generar_pdf', name='pdf_Ciudades'),
)