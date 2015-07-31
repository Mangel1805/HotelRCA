from django.shortcuts import render
from apps.sistema.models import ServicioCliente
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarServicio(CreateView):
	template_name='servicio/crear.html'
	model=ServicioCliente
	success_url=reverse_lazy('listarServicio')

class modificarServicio(UpdateView):
	model=ServicioCliente
	template_name='servicio/editar.html'
	success_url=reverse_lazy('listarServicio')

class eliminarServicio(DeleteView):
	model=ServicioCliente
	context_object_name="servicios"
	template_name='servicio/eliminar.html'
	success_url=reverse_lazy('listarServicio')

class listarServicio(ListView):
	model=ServicioCliente
	template_name='servicio/listar.html'
	context_object_name='servicios'
