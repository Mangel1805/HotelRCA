# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.sistema.models import TipoHabitacion
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	

# Create your views here.


from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

class index(TemplateView):
	template_name='inicio/index.html'

class registrarTipoHabitacion(CreateView):
	template_name='tipoHabitacion/crear.html'
	model=TipoHabitacion
	success_url=reverse_lazy('listarTipoHabitacion')

class modificarTipoHabitacion(UpdateView):
	model=TipoHabitacion
	template_name='tipoHabitacion/editar.html'
	success_url=reverse_lazy('listarTipoHabitacion')

class eliminarTipoHabitacion(DeleteView):
	model=TipoHabitacion
	context_object_name="tipoHabitacion"
	template_name='tipoHabitacion/eliminar.html'
	success_url=reverse_lazy('listarTipoHabitacion')

class listarTipoHabitacion(ListView):
	model=TipoHabitacion
	template_name='tipoHabitacion/listar.html'
	context_object_name='tipoHabitacion'


def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "tipoHabitacion.pdf"  # llamado clientes
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
    Encabezado = Paragraph("Listado de tipo de habitaciones", estilo['Heading1'])
    Lista.append(Encabezado)
    titulos = ('Nombre','Descripcion')
    consulta = [(tip.nombre,tip.descripcion) for tip in TipoHabitacion.objects.all()]
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