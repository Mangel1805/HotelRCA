from django.contrib import admin
from models import *
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(EstadosCliente)
admin.site.register(DatosHotel)
admin.site.register(TipoHabitacion)
admin.site.register(EstadosHabitacion)
admin.site.register(EstadosReservacion)
admin.site.register(Habitacion)
admin.site.register(Reservacion)
admin.site.register(EstadosFactura)
admin.site.register(EstadosProducto)
admin.site.register(Productos)
admin.site.register(ServicioCliente)
admin.site.register(Factura)
admin.site.register(EstadosIngreso)
admin.site.register(Ingresos)
admin.site.register(EstadosEgresos)
admin.site.register(Egresos)


