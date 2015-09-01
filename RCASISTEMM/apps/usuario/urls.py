from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', index.as_view(),name='home'),
    #********************Servicio*********************************************
   
    url(r'^$', index.as_view(),name='home'),
   
    url(r'^modificar/(?P<pk>[\d]+)$', modificarUsuario.as_view(),name='editarUsuario'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarUsuario.as_view(),name='eliminarUsuario'),
    url(r'^listar/$', listarUsuario.as_view(),name='listarUsuario'),
    url(r'^generar_pdf/$','apps.usuario.views.generar_pdf', name='pdf_Usuario'),
)