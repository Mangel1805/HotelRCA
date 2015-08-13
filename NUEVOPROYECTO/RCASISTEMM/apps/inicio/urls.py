from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
   
    #********************Producto*********************************************
   
  

   #login
    url(r'^$','django.contrib.auth.views.login',{'template_name':'inicio/index.html'},name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^registrarse/$', Registrarse.as_view() , name = 'registrarse'),
    

 #  url(r'^$', 'apps.inicio.views.inicio'),
    url(r'^nosotros/$', 'apps.inicio.views.nosotros'),
    url(r'^galeria/$', 'apps.inicio.views.galeria'),
    url(r'^servicios/$', 'apps.inicio.views.servicios'),
    url(r'^contactenos/$', 'apps.inicio.views.contactenos'),
    url(r'^sistema/$', 'apps.inicio.views.sistema'),
   # url(r'^login/$', 'apps.inicio.views.login'),
    #url(r'^registrarse/$', 'apps.inicio.views.registrarse'),
    url(r'^reservacion/$', 'apps.inicio.views.reservacion'),
    url(r'^imprimir/$', 'apps.inicio.views.imprimir'),
   
    
)