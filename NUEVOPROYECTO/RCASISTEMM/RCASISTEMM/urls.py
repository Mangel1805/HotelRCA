from django.conf.urls import patterns, include, url
from django.contrib import admin
#from apps.inicio.views import inicio
urlpatterns = patterns('',
     
    #Fachada 
    url(r'^' , include('apps.inicio.urls')),
    
    #admin
    url(r'^admin/', include(admin.site.urls)),

    #sistema
    #url(r'^$',include('apps.inicio.urls')),
    url(r'^hotel/',include('apps.datosHotel.urls')),
    url(r'^cliente/',include('apps.sistema.urls')),
    url(r'^ingreso/',include('apps.ingresos.urls')),
    url(r'^egreso/',include('apps.egresos.urls')),
    url(r'^producto/',include('apps.productos.urls')),
    url(r'^categoriaHabitacion/',include('apps.categoriaHabitacion.urls')),
    url(r'^tipoHabitacion/',include('apps.tipohabitacion.urls')),
    url(r'^habitacion/',include('apps.habitaciones.urls')),
    url(r'^ciudad/',include('apps.ciudad.urls')),
    url(r'^servicio/',include('apps.servicios.urls')),
    url(r'^reservacion/',include('apps.reservaciones.urls')),
    url(r'^factura/',include('apps.facturas.urls')),
)
