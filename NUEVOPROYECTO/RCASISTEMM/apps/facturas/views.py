from django.shortcuts import render
from apps.sistema.models import Factura
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	


class index(TemplateView):
	template_name='inicio/index.html'

class crearFactura(CreateView):
	template_name='factura/crear.html'
	model=Factura
	success_url=reverse_lazy('listarFactura')

class editarFactura(UpdateView):
	model=Factura
	template_name='factura/editar.html'
	success_url=reverse_lazy('listarFactura')

class eliminarFactura(DeleteView):
	model=Factura
	context_object_name="facturas"
	template_name='factura/eliminar.html'
	success_url=reverse_lazy('listarFactura')

class listarFactura(ListView):
	model=Factura
	template_name='factura/listar.html'
	context_object_name='facturas'
