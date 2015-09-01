from django.db import models
from django.contrib.auth.models import User


class TipoCargo(models.Model):
    Tipo = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=140)

    def __unicode__(self):
		return self.Tipo

class Perfiles(models.Model):
	usuario = models.OneToOneField(User)
	telefono = models.IntegerField()
	correo = models.EmailField()
	direccion = models.CharField(max_length=140)
	cargo = models.ForeignKey(TipoCargo,blank=True,null=True)
	
	def __unicode__(self):
		return self.usuario.username

# #
# Usu_nombre
# Usu_ced
# Usu_contra
# Usu_nombre
# Usu_apellido
# Usu_recepcion
# Usu_estado