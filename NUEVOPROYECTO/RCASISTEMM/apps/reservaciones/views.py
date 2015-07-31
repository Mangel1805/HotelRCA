from django.shortcuts import render
from apps.sistema.models import Reservacion
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarReservacion(CreateView):
	template_name='reservacion/crear.html'
	model=Reservacion
	success_url=reverse_lazy('listarReservacion')

class modificarReservacion(UpdateView):
	model=Reservacion
	template_name='reservacion/editar.html'
	success_url=reverse_lazy('listarReservacion')

class eliminarReservacion(DeleteView):
	model=Reservacion
	context_object_name="reservaciones"
	template_name='reservacion/eliminar.html'
	success_url=reverse_lazy('listarReservacion')

class listarReservacion(ListView):
	model=Reservacion
	template_name='reservacion/listar.html'
	context_object_name='reservaciones'
