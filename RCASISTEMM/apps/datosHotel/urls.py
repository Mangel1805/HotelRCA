from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    # Examples:
    #url(r'^$', index.as_view(),name='home'),
    #********************Hotel*********************************************
    url(r'^$', index.as_view(),name='home'),
    url(r'^registrar/$', registrarHotel.as_view(),name='crearHotel'),
    url(r'^modificar/(?P<pk>[\d]+)$', modificarHotel.as_view(),name='editarHotel'),
    url(r'^eliminar/(?P<pk>[\d]+)$', eliminarHotel.as_view(),name='eliminarHotel'),
    url(r'^listar/$', listarHotel.as_view(),name='listarHotel'),
    #url(r'^generar_pdf/$','apps.Hotel.views.generar_pdf', name='pdf_Hoteles'),
)