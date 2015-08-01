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


class Categoria(models.Model):
    
    cat_nombre = models.CharField(max_length=40)
    cat_descripcion = models.CharField(max_length=70)
    
    def __unicode__(self):
        return self.cat_nombre +" "+ self.cat_descripcion

class Ciudad(models.Model):
    ciu_nombre = models.CharField(max_length=50)
    ciu_descripcion = models.CharField(max_length=140)

    def __unicode__(self):
		return self.ciu_nombre
class EstadosCliente(models.Model):
    est_cli_tipo=models.CharField(max_length=8)

    def __unicode__(self):
        return self.est_cli_tipo

class Cliente(models.Model):
    cli_cedula = models.CharField(max_length=10)
    cli_nombre = models.CharField(max_length=30)
    cli_apellido = models.CharField(max_length=30)
    cli_telefono = models.CharField(max_length=10)
    cli_direccion = models.CharField(max_length=80)
    cli_email = models.CharField(max_length=140)
    cli_ocupacion = models.CharField(max_length=20)
    cli_estado = models.ForeignKey(EstadosCliente,blank=True, null=True)
    ciu_codigo = models.ForeignKey(Ciudad,blank=True, null=True)
    def __unicode__(self):
		return self.cli_nombre
    


class DatosHotel(models.Model):
    dat_ruc = models.CharField(max_length=13)
    dat_direccion = models.CharField(max_length=70)
    dat_telefono = models.CharField(max_length=10)
    dat_organigrama = models.CharField(max_length=60)



class TipoHabitacion(models.Model):
    tip_hab_nombre = models.CharField(max_length=50)
    tip_hab_descripcion = models.CharField(max_length=70)
    
    def __unicode__(self):
        return self.tip_hab_nombre+" "+self.tip_hab_descripcion

class EstadosHabitacion(models.Model):
    est_habi_tipo=models.CharField(max_length=8)

    def __unicode__(self):
        return self.est_habi_tipo

class EstadosReservacion(models.Model):
    est_rec_tipo=models.CharField(max_length=8)

    def __unicode__(self):
        return self.est_rec_tipo

class Habitacion(models.Model):
    hab_numero= models.IntegerField()
    id_tip_hab = models.ForeignKey(TipoHabitacion, blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, blank=True, null=True)
    hab_precio = models.FloatField()
    hab_estado = models.ForeignKey(EstadosHabitacion, blank=True, null=True)

    def __unicode__(self):
        return str(self.hab_numero)+str(self.id_tip_hab)

class Reservacion(models.Model):
    id_hab_numero = models.ForeignKey(Habitacion, blank=True, null=True)
    cli_codigo = models.ForeignKey(Cliente, blank=True, null=True)
    rec_fecha_inicio = models.DateField()
    rec_fecha_fin = models.DateField()
    rec_estado = models.ForeignKey(EstadosReservacion, blank=True, null=True)
    def __unicode__(self):
        return str(self.id_hab_numero)
class EstadosFactura(models.Model):
    est_fact_tipo=models.CharField(max_length=8)

    def __unicode__(self):
        return self.est_fact_tipo

class EstadosProducto(models.Model):
    est_pro_tipo=models.CharField(max_length=8)
  
    def __unicode__(self):
        return self.est_pro_tipo

class Productos(models.Model):
    pro_nombre = models.CharField(max_length=30)
    pro_descripcion = models.CharField(max_length=60)
    pro_costo = models.FloatField()
    pro_estado = models.ForeignKey(EstadosProducto,blank=True,null=True)
    def __unicode__(self):
        return self.pro_nombre

class ServicioCliente(models.Model):
    id_productos = models.ForeignKey(Productos, blank=True, null=True)
    cli_codigo = models.ForeignKey(Cliente, blank=True, null=True)
    ser_cantidad = models.IntegerField()
    ser_total = models.FloatField()
    def __unicode__(self):
        return str(self.id_productos)
    

class Factura(models.Model):
    fac_fecha = models.DateField()
    fac_subtotal = models.FloatField()
    fac_iva = models.FloatField()
    fac_total = models.FloatField()
    fac_estado = models.ForeignKey(EstadosFactura, blank=True, null=True)
    id_Reservacion = models.ForeignKey(Reservacion, blank=True, null=True)
    id_servicio = models.ForeignKey(ServicioCliente, blank=True, null=True)


class EstadosIngreso(models.Model):
    est_ing_tipo=models.CharField(max_length=8)
    
    def __unicode__(self):
        return self.est_ing_tipo

class Ingresos(models.Model):
    ing_fecha = models.DateField()
    ing_detalle = models.CharField(max_length=70)
    ing_tipo = models.CharField(max_length=40)
    ing_valor = models.FloatField()
    ing_estado = models.ForeignKey(EstadosIngreso,blank=True,null=True)


class EstadosEgresos(models.Model):
    est_egr_tipo=models.CharField(max_length=8)

    def __unicode__(self):
        return self.est_egr_tipo

class Egresos(models.Model):
    egr_fecha = models.DateField()
    egr_articulo = models.CharField(max_length=50)
    egr_tipo = models.CharField(max_length=30)
    egr_detalle = models.CharField(max_length=80)
    egr_cantidad = models.IntegerField()
    egr_precio_unitario = models.FloatField()
    egr_precio_total = models.FloatField()
    egr_estado = models.ForeignKey(EstadosEgresos, blank=True, null=True)






    




   
