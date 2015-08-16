from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************Reservacion*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarReservacion,name='crearReservacion'),
    url(r'^guardar/$', guardarReservacion,name='guardarReservacion'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarReservacion.as_view(),name='editarReservacion'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarReservacion.as_view(),name='eliminarReservacion'),
    url(r'^listar/$', listarReservacion.as_view(),name='listarReservacion'),
    url(r'^generar_pdf/$','apps.reservaciones.views.generar_pdf', name='pdf_Reservaciones'),
  #  url(r'^registrar/$',registrarReservacion,name='crearReservacion'),
    
)