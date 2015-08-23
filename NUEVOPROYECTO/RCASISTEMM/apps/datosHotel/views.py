# -*- coding: utf-8 -*-

from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table


from django.shortcuts import render,render_to_response
from apps.sistema.models import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarHotel(CreateView):
	template_name='inicio/datosHotel.html'
	model=DatosHotel
	success_url=reverse_lazy('home')

class modificarHotel(UpdateView):
	model=DatosHotel
	template_name='inicio/datosHotel.html'
	success_url=reverse_lazy('listarHotel')

class eliminarHotel(DeleteView):
	model=DatosHotel
	context_object_name="Hotel"
	template_name='inicio/eliminar.html'
	success_url=reverse_lazy('listarHotel')

class listarHotel(ListView):
	model=DatosHotel
	template_name='inicio/Informacion.html'
	context_object_name='Hotel'
    # def get_context_data(self, **kwargs):
    #     ctx = super(listarCiudad, self).get_context_data(**kwargs)
    #     ctx['clientes'] = Cliente.objects.all()
    #     ctx['articulos'] = Habitacion.objects.all()
    #     return ctx