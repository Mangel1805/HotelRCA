from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SonytelSistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', index.as_view(),name='home'),
    #********************CategoriaHabitacion*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarCategoriaHabitacion.as_view(),name='crearCategoriaHabitacion'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarCategoriaHabitacion.as_view(),name='editarCategoriaHabitacion'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarCategoriaHabitacion.as_view(),name='eliminarCategoriaHabitacion'),
    url(r'^listar/$', listarCategoriaHabitacion.as_view(),name='listarCategoriaHabitacion'),
    url(r'^generar_pdf/$','apps.categoriaHabitacion.views.generar_pdf', name='pdf_categoriaHabitaciones'),
)