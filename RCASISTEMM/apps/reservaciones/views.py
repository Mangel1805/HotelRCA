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
from django.db.models import Q

# Create your views here.



class index(TemplateView):
	template_name='inicio/index.html'

def registrarReservacion(request):
    estadoHabitacion = EstadosHabitacion.objects.get(estado='Inactivo')
    estadoCliente=EstadosCliente.objects.get(estado='Activo')
    print estadoHabitacion
    cntx={'listarHabitacion':Habitacion.objects.filter(estado=estadoHabitacion).order_by("id"),'listarclientes':Cliente.objects.filter(estado=estadoCliente).order_by("id")}
    print cntx
    return render_to_response('reservacion/crear.html', cntx,context_instance=RequestContext(request))



def registrarReservacionTempo(request):
    estadoHabitacion = EstadosHabitacion.objects.get(estado='Inactivo')
    estadoCliente=EstadosCliente.objects.get(estado='Activo')
    print estadoHabitacion
    cntx={'listarHabitacion':Habitacion.objects.filter(estado=estadoHabitacion).order_by("id"),'listarclientes':Cliente.objects.filter(estado=estadoCliente).order_by("id")}
    print cntx
    return render_to_response('reservacion/crearFicticia.html', cntx,context_instance=RequestContext(request))




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
    laHabitacion.estado=EstadosHabitacion.objects.get(estado='Activo')
    laHabitacion.save()
    print (str(laHabitacion)+"paso a Activa")
    
    return render_to_response('reservacion/c.html',context_instance=RequestContext(request))




def guardarFicticiaXCliente(request):
    print "ENTROOOOO :V :v "
    cedula = request.GET['cedula']
    print cedula
    nombre = request.GET['nombre']
    print nombre
    apellido = request.GET['apellido']
    print apellido
    direccion = request.GET['direccion']
    print direccion
    telefono = request.GET['telefono']
    print telefono
    habitacion=request.GET['Numerohabitacion']
    ciudad = request.GET['ciudad']
    print ciudad
    laHabitacion = Habitacion.objects.get(habitacion=request.GET['Numerohabitacion'])
    print laHabitacion
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
    
    fic=Ficticia(
        cedula=cedula,
        nombre=nombre,
        apellido=apellido,
        telefono=telefono,
        direccion=direccion,
        habitacion=habitacion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        adultos=adultos,
        ninos=ninos,
        precio=total

        )
    fic.save()
    print str("Se Guardo")
    
    return render_to_response('reservacion/c.html',context_instance=RequestContext(request))


    

def guardarReservacionTempo(request):
    print "ENTROOOOO :V :v "
   
    ficticia=request.GET['ficticia']
    print ficticia
    cedula= request.GET['cedula']
    print cedula
    nombre= request.GET['nombre']
    print nombre
    apellido= request.GET['apellido']
    print apellido
    telefono= request.GET['telefono']
    print telefono
    direccion= request.GET['direccion']
    print direccion
    habitacion= request.GET['habitacion']
    print habitacion
    fecha_inicio= request.GET['fecha_inicio']
    print fecha_inicio
    fecha_fin= request.GET['fecha_fin']
    print fecha_fin
    adultos= request.GET['adultos']
    print adultos
    ninos= request.GET['ninos']
    print ninos
    precio= request.GET['precio']
    print precio
   
    es=EstadosReservacion.objects.get(estado='Activo')
    print es
    cli=EstadosCliente.objects.get(estado='Activo')
    print cli
    fic=Ficticia.objects.get(id=ficticia)
    print "el id de la ficticia"+str(fic)
    laHabitacion = Habitacion.objects.get(habitacion=request.GET['habitacion'])
    print laHabitacion
    try:
              
        unCliente= Cliente.objects.get(cedula=cedula)
        print "guarda solo la recepcion"
        r=Reservacion(
            habitacion=laHabitacion,
            cliente=unCliente,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            adultos=adultos,
            ninos=ninos,
            precio=precio,
            estado=es,
            )
        r.save()
        print str("Se Guardo")
        
        fic.delete()
        print "se elimino la ficiticia"
        print str("Se Guardo")
        laHabitacion.estado=EstadosHabitacion.objects.get(estado='Activo')
        laHabitacion.save()
        print (str(laHabitacion)+"paso a Activa")
    
    except Exception, e:
        print "guarda todo"
        cliente=Cliente(cedula=cedula,nombre=nombre,apellido=apellido,telefono=telefono,direccion=direccion,email='',estado=EstadosCliente.objects.get(estado='Activo'))
        cliente.save()
        print "se guardo Cliente"
        cli= Cliente.objects.get(cedula=cedula)
        print (str(cli)+" actual guardado")
        r=Reservacion(
            habitacion=laHabitacion,
            cliente=cli,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            adultos=adultos,
            ninos=ninos,
            precio=precio,
            estado=es,
            )
        r.save()
        print str("Se Guardo")  
        print str("Se Guardo reservacion")
        
        fic.delete()
        print "se elimino la ficiticia"
        print str("Se Guardo")
        laHabitacion.estado=EstadosHabitacion.objects.get(estado='Activo')
        laHabitacion.save()
        print (str(laHabitacion)+"paso a Activa")
    return render_to_response('reservacion/listar.html',context_instance=RequestContext(request))

class modificarReservacion(UpdateView):
	model=Reservacion
	template_name='reservacion/editar.html'
	success_url=reverse_lazy('listarReservacion')

def cambiarEstado(request):
    print "ENTROOOOO :V :v "
    numero=request.GET['Numerohabitacion']
    print numero
    laHabitacion = Habitacion.objects.get(habitacion=request.GET['Numerohabitacion'])
    print laHabitacion
    print "continua"
    laHabitacion.estado=EstadosHabitacion.objects.get(estado='Inactivo')
    laHabitacion.save()
    print (str(laHabitacion)+"paso a Inactivo")
    print str("Se Guardo")

    
    return render_to_response('reservacion/listar.html',context_instance=RequestContext(request))




class eliminarReservacion(DeleteView):
    model=Reservacion
    context_object_name="reservaciones"
    template_name='reservacion/eliminar.html'
    success_url=reverse_lazy('listarReservacion')
    def get_context_data(self,**kwargs):
        ctx = super(eliminarReservacion, self).get_context_data(**kwargs)
        ctx['listarhabitacion'] = Habitacion.objects.filter(estado=EstadosHabitacion.objects.get(estado='Activo'))
        print ctx
        return ctx


class eliminarReservacionFicticia(DeleteView):
    model=Ficticia
    context_object_name="ficticia"
    template_name='reservacion/eliminarFicticia.html'
    success_url=reverse_lazy('listarReservacion')

class listarReservacion(ListView):
    model=Reservacion
    template_name='reservacion/listar.html'
    context_object_name='reservaciones'
    def get_context_data(self,**kwargs):
        ctx = super(listarReservacion, self).get_context_data(**kwargs)
        ctx['ficticia'] = Ficticia.objects.all()
        ctx['listarclientes'] = Cliente.objects.all()
        ctx['listarReservacion'] = Reservacion.objects.filter(estado=EstadosReservacion.objects.get(estado='Activo'))
        return ctx

class buscarReservacion(TemplateView):
    def get(self,request,*args,**kwargs):
        buscar = request.GET.get('nombre')
        print buscar

        clie=Cliente.objects.filter(cedula__icontains=buscar)
        print clie
        habi=Habitacion.objects.filter(Q(habitacion__icontains=buscar))
        print habi
        est=EstadosReservacion.objects.get(estado='Activo')
        print est
        reservacion = Reservacion.objects.filter((Q(cliente__icontains=clie)|Q(habitacion__icontains=habi))&Q(estado=est)).order_by("id")
        print reservacion
        data = serializers.serialize('json',reservacion,fields=('habitacion','cliente','fecha_inicio','fecha_fin','adultos','ninos','precio','estado'))
        return HttpResponse(data,content_type='application/json')
           


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