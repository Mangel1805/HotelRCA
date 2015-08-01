from django.conf.urls import patterns, include, url
from .views import crearFactura,index,crearFactura,editarFactura,eliminarFactura,listarFactura
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************Factura*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', crearFactura.as_view(),name='crearFactura'),
    url(r'^modificar/(?P<pk>[\d]+)$', editarFactura.as_view(),name='editarFactura'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarFactura.as_view(),name='eliminarFactura'),
    url(r'^listar/$', listarFactura.as_view(),name='listarFactura'),

    #*********************PROVEEDOR***************************************
    
    
)