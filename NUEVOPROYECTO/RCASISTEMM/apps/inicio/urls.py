from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
   
    #********************Producto*********************************************
   
  

   #login
    url(r'^$','django.contrib.auth.views.login',{'template_name':'inicio/index.html'},name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^registrarse/$', Registrarse.as_view() , name = 'registrarse'),
    

 #  url(r'^$', 'apps.inicio.views.inicio'),
    url(r'^nosotros/$',  nosotros.as_view(),name='nosotros'),
    url(r'^detalles/$',  detalles.as_view(),name='detalles'),
    url(r'^galeria/$',   galeria.as_view(),name='galeria'),
    url(r'^servicios/$',servicios.as_view(),name='servicios'),
    url(r'^contactenos/$',  contactenos.as_view(),name='contactenos'),
    url(r'^sistema/$', sistema.as_view(),name='sistema'),

   
    
)