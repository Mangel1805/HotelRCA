from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************Reservacion*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarReservacion.as_view(),name='crearReservacion'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarReservacion.as_view(),name='editarReservacion'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarReservacion.as_view(),name='eliminarReservacion'),
    url(r'^listar/$', listarReservacion.as_view(),name='listarReservacion'),

   
    
)