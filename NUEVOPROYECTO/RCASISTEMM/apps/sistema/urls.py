from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CLIENTE*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', crearCliente.as_view(),name='crearCliente'),
    url(r'^modificar/(?P<pk>[\d]+)$', editarCliente.as_view(),name='editarCliente'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarCliente.as_view(),name='eliminarCliente'),
    url(r'^listar/$', listarCliente.as_view(),name='listarCliente'),
    url(r'^generar_pdf/$','apps.sistema.views.generar_pdf', name='pdf_Clientes'),
    #*********************PROVEEDOR***************************************
    
    
)