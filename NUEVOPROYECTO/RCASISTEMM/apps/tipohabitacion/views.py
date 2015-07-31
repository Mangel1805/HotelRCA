from django.shortcuts import render
from apps.sistema.models import TipoHabitacion
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarTipoHabitacion(CreateView):
	template_name='tipoHabitacion/crear.html'
	model=TipoHabitacion
	success_url=reverse_lazy('listarTipoHabitacion')

class modificarTipoHabitacion(UpdateView):
	model=TipoHabitacion
	template_name='tipoHabitacion/editar.html'
	success_url=reverse_lazy('listarTipoHabitacion')

class eliminarTipoHabitacion(DeleteView):
	model=TipoHabitacion
	context_object_name="tipoHabitacion"
	template_name='tipoHabitacion/eliminar.html'
	success_url=reverse_lazy('listarTipoHabitacion')

class listarTipoHabitacion(ListView):
	model=TipoHabitacion
	template_name='tipoHabitacion/listar.html'
	context_object_name='tipoHabitacion'
