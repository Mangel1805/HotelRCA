# -*- coding: utf-8 -*-
from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from apps.sistema.models import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from .forms import reservacionForm
# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

# class registrarReservacion(CreateView):
# 	template_name='reservacion/crear.html'
# 	model=Reservacion
# 	success_url=reverse_lazy('listarReservacion')

def registrarReservacion(request):
    estadoHabitacion = EstadosHabitacion.objects.get(estado='Activo')
   
    estadoCliente=EstadosCliente.objects.get(estado='Activo')
   
    print estadoHabitacion
    cntx={'listarHabitacion':Habitacion.objects.filter(estado=estadoHabitacion),'listarclientes':Cliente.objects.filter(estado=estadoCliente)}
    print cntx
    
    return render_to_response('reservacion/regis.html', cntx,context_instance=RequestContext(request))
    



def registrarReservacionss(request):
    estados=EstadosReservacion.objects.all()
    if request.method=="POST":
        form=reservacionForm(request.POST)
        if form.is_valid():
            enlace=form.save(commit=False)
            enlace.save()
            return HttpResponseRedirect("/reservacion/listar/")
    else:
        form=reservacionForm()
    template="reservacion/crear.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


def guardarReservacion(request):
    print "ENTROOOOO :V :v "
    cedula = request.GET['cedula']
    print cedula
    
    
    
   
    laHabitacion = Habitacion.objects.get(habitacion=request.GET['Numerohabitacion'])
    print laHabitacion
    unCliente= Cliente.objects.get(cedula=cedula)
    print str(unCliente.id)+" "+str(unCliente.cedula)+" "+str(unCliente.nombre)
    fecha_inicio= request.GET['fecha_inicio']
    print fecha_inicio
    fecha_fin = request.GET['fecha_fin']
    print fecha_fin
    adultos = request.GET['Nadultos']
    print adultos
    ninos = request.GET['Nninos']
    print ninos
    total =request.GET['total']
    print total
    es=EstadosReservacion.objects.get(estado='Activo')
    print es
    print "continua"
    

    

    reser=Reservacion(
        habitacion=laHabitacion,
        cliente=unCliente,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        adultos=request.GET['Nadultos'],
        ninos=request.GET['Nninos'],
        precio=request.GET['total'],
        estado=EstadosReservacion.objects.get(estado='Activo')

        )
    reser.save()
    print str("Se Guardo")
    
    return render_to_response('reservacion/c.html',context_instance=RequestContext(request))

    





class modificarReservacion(UpdateView):
	model=Reservacion
	template_name='reservacion/editar.html'
	success_url=reverse_lazy('listarReservacion')

class eliminarReservacion(DeleteView):
	model=Reservacion
	context_object_name="reservaciones"
	template_name='reservacion/eliminar.html'
	success_url=reverse_lazy('listarReservacion')

class listarReservacion(ListView):
	model=Reservacion
	template_name='reservacion/listar.html'
	context_object_name='reservaciones'


def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Reservaciones.pdf"  # llamado clientes
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
    Encabezado = Paragraph("Listado de reservaciones", estilo['Heading1'])
    Lista.append(Encabezado)
    titulos = ('Habitación','Cliente','Adultos','Niños','Precio','Fecha Inicio','Fecha Fin','Estado')
    consulta = [(aux.habitacion,aux.cliente,aux.adultos,aux.ninos,aux.precio,aux.fecha_inicio,aux.fecha_fin,aux.estado) for aux in Reservacion.objects.all()]
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