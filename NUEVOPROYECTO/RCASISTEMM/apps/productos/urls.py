from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************Producto*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarProducto.as_view(),name='crearProducto'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarProducto.as_view(),name='editarProducto'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarProducto.as_view(),name='eliminarProducto'),
    url(r'^listar/$', listarProducto.as_view(),name='listarProducto'),

   
    
)