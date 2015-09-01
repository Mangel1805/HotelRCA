from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', index.as_view(),name='home'),
    #********************Reservacion*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarReservacion,name='crearReservacion'),
    url(r'^temporal/$', registrarReservacionTempo,name='crearReservacionTemporal'),
    url(r'^guardarFicticia/$', guardarReservacionTempo,name='guardarReservacionTempo'),
    url(r'^guardarFicticiaXCliente/$', guardarFicticiaXCliente,name='guardarFicticiaXCliente'),
    url(r'^guardar/$', guardarReservacion,name='guardarReservacion'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarReservacion.as_view(),name='editarReservacion'),
    url(r'^cambiarEstado/$', cambiarEstado,name='cambiarEstado'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarReservacion.as_view(),name='eliminarReservacion'),
    url(r'^eliminarFicticia/(?P<pk>[\d]+)$', eliminarReservacionFicticia.as_view(),name='eliminarReservacionFicticia'),
    url(r'^listar/$', listarReservacion.as_view(),name='listarReservacion'),
    url(r'^buscar/$', buscarReservacion.as_view(),name='buscarReservacion'),
    url(r'^generar_pdf/$','apps.reservaciones.views.generar_pdf', name='pdf_Reservaciones'),
  #  url(r'^registrar/$',registrarReservacion,name='crearReservacion'),
    
)