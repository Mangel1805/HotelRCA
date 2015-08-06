from django.shortcuts import render
from apps.sistema.models import Cliente
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


class index(TemplateView):
	template_name='inicio/index.html'

class crearCliente(CreateView):
	template_name='cliente/crear.html'
	model=Cliente
	success_url=reverse_lazy('listarCliente')

class editarCliente(UpdateView):
	model=Cliente
	template_name='cliente/editar.html'
	success_url=reverse_lazy('listarCliente')

class eliminarCliente(DeleteView):
	model=Cliente
	context_object_name="cliente"
	template_name='cliente/eliminar.html'
	success_url=reverse_lazy('listarCliente')

class listarCliente(ListView):
	model=Cliente
	template_name='cliente/listar.html'
	context_object_name='clientes'
