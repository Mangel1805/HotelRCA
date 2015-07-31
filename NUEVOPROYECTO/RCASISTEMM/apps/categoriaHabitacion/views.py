from django.shortcuts import render
from apps.sistema.models import Categoria
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarCategoriaHabitacion(CreateView):
	template_name='categoriaHabitacion/crear.html'
	model=Categoria
	success_url=reverse_lazy('listarCategoriaHabitacion')

class modificarCategoriaHabitacion(UpdateView):
	model=Categoria
	template_name='categoriaHabitacion/editar.html'
	success_url=reverse_lazy('listarCategoriaHabitacion')

class eliminarCategoriaHabitacion(DeleteView):
	model=Categoria
	context_object_name="categoriaHabitacion"
	template_name='categoriaHabitacion/eliminar.html'
	success_url=reverse_lazy('listarCategoriaHabitacion')

class listarCategoriaHabitacion(ListView):
	model=Categoria
	template_name='categoriaHabitacion/listar.html'
	context_object_name='categoriaHabitacion'
