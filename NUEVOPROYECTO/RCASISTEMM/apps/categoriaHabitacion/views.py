# -*- coding: utf-8 -*-

from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

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


def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Categoria Habitacion.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=40,
                            bottomMargin=18,
                            )
    Lista = []
    estilo = getSampleStyleSheet()
    Encabezado = Paragraph("Listado de Categorías de Habitaciones", estilo['Heading1'])
    Lista.append(Encabezado)
    titulos = ('Nombre','Descripción')
    consulta = [(aux.nombre,aux.descripcion) for aux in Categoria.objects.all()]
    print consulta

    tabla = Table([titulos] + consulta)
    tabla.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (8, -1), 1, colors.black),#cuadricula
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),#lineadebajo del titulos
            ('BACKGROUND', (0, 0), (-1, 0), colors.brown)
            
        ]
    ))
    Lista.append(tabla)
    doc.build(Lista)
    response.write(buff.getvalue())
    buff.close()
    return response