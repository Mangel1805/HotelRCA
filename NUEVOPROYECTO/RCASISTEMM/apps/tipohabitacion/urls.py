from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************TipoHabitacion*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarTipoHabitacion.as_view(),name='crearTipoHabitacion'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarTipoHabitacion.as_view(),name='editarTipoHabitacion'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarTipoHabitacion.as_view(),name='eliminarTipoHabitacion'),
    url(r'^listar/$', listarTipoHabitacion.as_view(),name='listarTipoHabitacion'),
)