from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', index.as_view(),name='home'),
    #********************Factura*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^imprimir/$', imprimir.as_view(),name='imprimir'),
    #url(r'^registrar/$', crearFactura.as_view(),name='crearFactura'),


    url(r'^registrar/$', generarVentaFactura,name='crearFactura'),
    url(r'^guardar/$', guardarFactura,name='guargarFactura'),
    url(r'^guardarFact/$', guardarUnaFactura,name='guardarunaFactura'),
    url(r'^modificar/(?P<pk>[\d]+)$', editarFactura.as_view(),name='editarFactura'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarFactura.as_view(),name='eliminarFactura'),
    url(r'^listar/$', listarFactura.as_view(),name='listarFactura'),
    url(r'^buscar/$', buscarFactura.as_view(),name='buscarFactura'),
    url(r'^generar_pdf/$','apps.facturas.views.generar_pdf', name='pdf_Facturas'),
    
    
    
)