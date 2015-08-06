from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.inicio.views import inicio
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RCASISTEMM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   
    #Fachada 
    url(r'^$', inicio),
    url(r'^inicio/$', 'apps.inicio.views.inicio'),
    url(r'^nosotros/$', 'apps.inicio.views.nosotros'),
    url(r'^galeria/$', 'apps.inicio.views.galeria'),
    url(r'^servicios/$', 'apps.inicio.views.servicios'),
    url(r'^contactenos/$', 'apps.inicio.views.contactenos'),
    url(r'^sistema/$', 'apps.inicio.views.sistema'),
    url(r'^login/$', 'apps.inicio.views.login'),
    url(r'^registrarse/$', 'apps.inicio.views.registrarse'),
    url(r'^reservacion/$', 'apps.inicio.views.reservacion'),
    url(r'^imprimir/$', 'apps.inicio.views.imprimir'),
    #admin
    url(r'^admin/', include(admin.site.urls)),
    #sistema
    url(r'^cliente/',include('apps.sistema.urls')),
    url(r'^productos/',include('apps.productos.urls')),
    url(r'^categoriaHabitacion/',include('apps.categoriaHabitacion.urls')),
    url(r'^tipoHabitacion/',include('apps.tipohabitacion.urls')),
    url(r'^habitacion/',include('apps.habitaciones.urls')),
    url(r'^ciudad/',include('apps.ciudad.urls')),
    url(r'^servicio/',include('apps.servicios.urls')),
    url(r'^reservacion/',include('apps.reservaciones.urls')),
    url(r'^factura/',include('apps.facturas.urls')),
)
