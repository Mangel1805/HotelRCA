from django.shortcuts import render
from apps.sistema.models import Productos, EstadosProducto
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarProducto(CreateView):
	template_name='productos/crear.html'
	model=Productos
	success_url=reverse_lazy('listarProducto')

class modificarProducto(UpdateView):
	model=Productos
	template_name='productos/editar.html'
	success_url=reverse_lazy('listarProducto')

class eliminarProducto(DeleteView):
	model=Productos
	context_object_name="productos"
	template_name='productos/eliminar.html'
	success_url=reverse_lazy('listarProducto')

class listarProducto(ListView):
	model=Productos
	template_name='productos/listar.html'
	context_object_name='productos'
