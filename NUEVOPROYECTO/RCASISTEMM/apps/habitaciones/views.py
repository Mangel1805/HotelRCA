from django.shortcuts import render
from apps.sistema.models import Habitacion
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarHabitacion(CreateView):
	template_name='habitaciones/crear.html'
	model=Habitacion
	success_url=reverse_lazy('listarHabitacion')

class modificarHabitacion(UpdateView):
	model=Habitacion
	template_name='habitaciones/editar.html'
	success_url=reverse_lazy('listarHabitacion')

class eliminarHabitacion(DeleteView):
	model=Habitacion
	context_object_name="habitacion"
	template_name='habitaciones/eliminar.html'
	success_url=reverse_lazy('listarHabitacion')

class listarHabitacion(ListView):
	model=Habitacion
	template_name='habitaciones/listar.html'
	context_object_name='habitacion'
