# -*- coding: utf-8 -*-

from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table


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



def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Factuaras.pdf"  # llamado clientes
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
    Encabezado = Paragraph("Listado de Facturas", estilo['Heading1'])
    Lista.append(Encabezado)
    titulos = ('ID','Fecha','Subtotal','Iva','Total','Estado','Reservacion')
    consulta = [(aux.id,aux.fecha,aux.subtotal,aux.iva,aux.total,aux.estado,aux.reservacion) for aux in Factura.objects.all()]
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