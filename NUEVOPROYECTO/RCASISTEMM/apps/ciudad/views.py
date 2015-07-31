from django.shortcuts import render
from apps.sistema.models import Ciudad
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarCiudad(CreateView):
	template_name='ciudad/crear.html'
	model=Ciudad
	success_url=reverse_lazy('listarCiudad')

class modificarCiudad(UpdateView):
	model=Ciudad
	template_name='ciudad/editar.html'
	success_url=reverse_lazy('listarCiudad')

class eliminarCiudad(DeleteView):
	model=Ciudad
	context_object_name="ciudad"
	template_name='ciudad/eliminar.html'
	success_url=reverse_lazy('listarCiudad')

class listarCiudad(ListView):
	model=Ciudad
	template_name='ciudad/listar.html'
	context_object_name='ciudad'
