# -*- coding: utf-8 -*-

from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

from django.shortcuts import render
from apps.sistema.models import Habitacion
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.db.models import Q
# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

class registrarHabitacion(CreateView):
	template_name='habitaciones/crear.html'
	model=Habitacion
	success_url=reverse_lazy('listarHabitacion')

class modificarHabitacion(UpdateView):
	model=Habitacion
	template_name='habitaciones/editar.html'
	success_url=reverse_lazy('listarHabitacion')

class eliminarHabitacion(DeleteView):
	model=Habitacion
	context_object_name="habitacion"
	template_name='habitaciones/eliminar.html'
	success_url=reverse_lazy('listarHabitacion')

class listarHabitacion(ListView):
	model=Habitacion
	template_name='habitaciones/listar.html'
	context_object_name='habitacion'

class buscarHabitacion(TemplateView):
    def get(self,request,*args,**kwargs):
        buscar = request.GET.get('nombre')
        print buscar
        produc = Habitacion.objects.filter(Q(habitacion__icontains=buscar)).order_by("id")
        print produc
        data = serializers.serialize('json',produc,fields=('habitacion','tipo','categoria','precio','estado'))
        return HttpResponse(data,content_type='application/json')

def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "habitaciones.pdf"  # llamado clientes
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
    Encabezado = Paragraph("Listado de Habitaciones", estilo['Heading1'])
    Lista.append(Encabezado)
    titulos = ('Habitacion','Tipo','Categoria','Precio','Estado')
    consulta = [(aux.habitacion,aux.tipo,aux.categoria,aux.precio,aux.estado) for aux in Habitacion.objects.all()]
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