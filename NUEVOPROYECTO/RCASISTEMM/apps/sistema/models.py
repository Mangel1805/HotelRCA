# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=70)
    
    def __unicode__(self):
        return self.nombre +" "+ self.descripcion

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=140)

    def __unicode__(self):
		return self.nombre

class EstadosCliente(models.Model):
    estado=models.CharField(max_length=8)

    def __unicode__(self):
        return self.estado

class Cliente(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10, blank=True)
    direccion = models.CharField(max_length=80)
    email  = models.EmailField()
    ocupacion = models.CharField(max_length=20)
    estado = models.ForeignKey(EstadosCliente,blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad,blank=True, null=True)
    def __unicode__(self):
		return self.nombre +" "+ self.apellido
    


class DatosHotel(models.Model):
    ruc = models.CharField(max_length=13)
    direccion = models.CharField(max_length=140)
    telefono = models.CharField(max_length=10)
    organigrama = models.CharField(max_length=140)



class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=70)
    
    def __unicode__(self):
        return self.nombre+" "+self.descripcion

class EstadosHabitacion(models.Model):
    estado=models.CharField(max_length=8)

    def __unicode__(self):
        return self.estado

class EstadosReservacion(models.Model):
    estado=models.CharField(max_length=8)

    def __unicode__(self):
        return self.estado

class Habitacion(models.Model):
    habitacion= models.IntegerField()
    tipo = models.ForeignKey(TipoHabitacion, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True)
    precio = models.DecimalField(max_digits=8,decimal_places=2)
    estado = models.ForeignKey(EstadosHabitacion, blank=True, null=True)

    def __unicode__(self):
        return str(self.habitacion)+" "+str(self.tipo)

class Reservacion(models.Model):
    habitacion = models.ForeignKey(Habitacion, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    fecha_inicio  = models.DateField()
    fecha_fin = models.DateField()
    adultos = models.IntegerField()
    ninos = models.IntegerField()
    precio = models.DecimalField(max_digits=8,decimal_places=2)
    estado = models.ForeignKey(EstadosReservacion, blank=True, null=True)
    def __unicode__(self):
        return str(self.cliente)+" habitacion "+str(self.habitacion)

class EstadosFactura(models.Model):
    estado=models.CharField(max_length=8)

    def __unicode__(self):
        return self.estado

class EstadosProducto(models.Model):
    estado=models.CharField(max_length=8)
  
    def __unicode__(self):
        return self.estado

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    costo = models.DecimalField(max_digits=8,decimal_places=2)
    estado = models.ForeignKey(EstadosProducto,blank=True,null=True)
    def __unicode__(self):
        return self.nombre

class ServicioCliente(models.Model):
    habitacion = models.ForeignKey(Habitacion, blank=True, null=True)
    producto = models.ForeignKey(Productos, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=8,decimal_places=2)
    def __unicode__(self):
        return str(self.producto)
    

class Factura(models.Model):
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=8,decimal_places=2)
    iva = models.DecimalField(max_digits=8,decimal_places=2)
    total = models.DecimalField(max_digits=8,decimal_places=2)
    estado = models.ForeignKey(EstadosFactura, blank=True, null=True)
    reservacion = models.ForeignKey(Reservacion, blank=True, null=True)
    #id_servicio = models.ForeignKey(ServicioCliente, blank=True, null=True)
    def __unicode__(self):
        return str("Fact-000")+str(self.id)

class EstadosIngreso(models.Model):
    estado=models.CharField(max_length=8)
    
    def __unicode__(self):
        return self.estado

class Ingresos(models.Model):
    usuario = models.OneToOneField(User)
    fecha = models.DateField(auto_now_add=True)
    detalle = models.CharField(max_length=140)
    tipo = models.CharField(max_length=140)
    valor = models.DecimalField(max_digits=8,decimal_places=2)
    estado = models.ForeignKey(EstadosIngreso,blank=True,null=True)


class EstadosEgresos(models.Model):
    estado=models.CharField(max_length=8)

    def __unicode__(self):
        return self.estado

class Egresos(models.Model):
    usuario = models.OneToOneField(User)
    fecha = models.DateField(auto_now_add=True)
    articulo = models.CharField(max_length=140)
    tipo = models.CharField(max_length=140)
    detalle = models.CharField(max_length=140)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=8,decimal_places=2)
    precio_total = models.DecimalField(max_digits=8,decimal_places=2)
    estado = models.ForeignKey(EstadosEgresos, blank=True, null=True)


    
class FacturaServicios(models.Model):
    servico=models.ForeignKey(ServicioCliente,blank=True,null=True)
    factura=models.ForeignKey(Factura,blank=True,null=True)
    
    def __unicode__(self):
        return str("cod - ")+str(self.id)


       
