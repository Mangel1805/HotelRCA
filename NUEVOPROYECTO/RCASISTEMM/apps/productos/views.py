# -*- coding: utf-8 -*-

from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

from django.shortcuts import render
from apps.sistema.models import Productos
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

def generar_pdf(request):
    print "Genero el PDF productos"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "productos.pdf"  # llamado clientes
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
    cabeza = Paragraph("Listado de Productos", estilo['Heading3'])
    Encabezado = Paragraph("Listado de Productos", estilo['Heading1'])
    Lista.append(cabeza)
    Lista.append(Encabezado)
    titulos = ('Nombre','Descripcion','Costo','Estado')
    consulta = [(aux.nombre,aux.descripcion,aux.costo,aux.estado) for aux in Productos.objects.all()]
    print consulta

    tabla = Table([titulos] + consulta)
    tabla.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (8, -1), 1, colors.black),#cuadricula
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),#lineadebajo del titulos
            ('BACKGROUND', (0, 0), (-1, 0), colors.silver),
            ('FONTGROUND', (0, 0), (-1, 0), colors.silver)
            
        ]
    ))
    Lista.append(tabla)
    doc.build(Lista)
    response.write(buff.getvalue())
    buff.close()
    return response