from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RCASISTEMM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cliente/',include('apps.sistema.urls')),
    url(r'^productos/',include('apps.productos.urls')),
    url(r'^categoriaHabitacion/',include('apps.categoriaHabitacion.urls')),
    url(r'^tipoHabitacion/',include('apps.tipohabitacion.urls')),
    url(r'^habitacion/',include('apps.habitaciones.urls')),
    url(r'^ciudad/',include('apps.ciudad.urls')),
    url(r'^servicio/',include('apps.servicios.urls')),
    url(r'^reservacion/',include('apps.reservaciones.urls')),

)
