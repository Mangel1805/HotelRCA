# -*- coding: utf-8 -*-

from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

from django.shortcuts import render
from apps.sistema.models import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarIngreso(CreateView):
	template_name='ingresos/crear.html'
	model=Ingresos
	success_url=reverse_lazy('listarIngreso')

class modificarIngreso(UpdateView):
	model=Ingresos
	template_name='ingresos/editar.html'
	success_url=reverse_lazy('listarIngreso')

class eliminarIngreso(DeleteView):
	model=Ingresos
	context_object_name="ingresos"
	template_name='ingresos/eliminar.html'
	success_url=reverse_lazy('listarIngreso')


class listarIngreso(ListView):
    model=Ingresos
    template_name='ingresos/listar.html'
    context_object_name='ingresos'
    def get_context_data(self,**kwargs):
        ctx = super(listarIngreso, self).get_context_data(**kwargs)
        ctx['listarUsuarios'] = User.objects.all()
        return ctx

class buscarIngreso(TemplateView):
    def get(self,request,*args,**kwargs):
        print "entro"
        inicio = request.GET.get('inicio')
        fin = request.GET.get('fin')
        print inicio
        print fin
        ingreso = Ingresos.objects.filter(Q(fecha__range=(inicio,fin))).order_by("id")
        print ingreso
        data = serializers.serialize('json',ingreso,fields=('usuario','fecha','detalle','tipo','valor','estado'))
        return HttpResponse(data,content_type='application/json')

def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Ingresos.pdf"  # llamado clientes
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
    Encabezado = Paragraph("Listado de Ingresos", estilo['Heading1'])
    Lista.append(Encabezado)
    titulos = ('Usuario','Fecha','Detalle','Tipo','Valor','Estado')
    consulta = [(aux.usuario,aux.fecha,aux.detalle,aux.tipo,aux.valor,aux.estado) for aux in Ingresos.objects.all()]
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