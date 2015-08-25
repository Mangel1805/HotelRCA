from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************Habitacion*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarHabitacion.as_view(),name='crearHabitacion'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarHabitacion.as_view(),name='editarHabitacion'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarHabitacion.as_view(),name='eliminarHabitacion'),
    url(r'^listar/$', listarHabitacion.as_view(),name='listarHabitacion'),
    url(r'^buscar/$', buscarHabitacion.as_view(),name='buscarHabitacion'),
    url(r'^generar_pdf/$','apps.habitaciones.views.generar_pdf', name='pdf_Habitaciones'),
)