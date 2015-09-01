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
#from django.template import Context, Template,RequestContext

class index(TemplateView):
	template_name='factura/fa.html'


class imprimir(TemplateView):
    template_name='factura/fa.html'
    def get_context_data(self,**kwargs):
        ctx = super(imprimir, self).get_context_data(**kwargs)
        ctx['listarClientes'] = Cliente.objects.all()
        ctx['nFactura'] = Factura.objects.all().count()
        numero=Factura.objects.all().count()
        ctx['listarFacturas'] = Factura.objects.get(id=numero)
        ctx['listarserviciosFac'] = FacturaServicios.objects.filter(factura=numero)
        ctx['listarservicios'] = ServicioCliente.objects.all()
        ctx['listarReservacion'] = Reservacion.objects.all()
        ctx['listarProductos'] = Productos.objects.all()
        ctx['listarHabitacion'] = Habitacion.objects.all()
        print ctx
     
        return ctx

def generarVentaFactura(request):
    estadoHabitacion = EstadosHabitacion.objects.get(estado='Activo')
    estadoProducto = EstadosProducto.objects.get(estado='Activo')
    estadoCliente=EstadosCliente.objects.get(estado='Activo')
    estadoReservacion=EstadosCliente.objects.get(estado='Activo')
    estadoServicio=EstadosServicio.objects.get(estado='Activo')
    print estadoHabitacion
    cntx={'listarHabitacion':Habitacion.objects.filter(estado=estadoHabitacion),'listarclientes':Cliente.objects.filter(estado=estadoCliente), 
          'listarproductos':Productos.objects.filter(estado=estadoProducto), 'nFactura': 1+Factura.objects.count(),
          'listaServicios':ServicioCliente.objects.filter(estado=estadoServicio),'listaReservacion':Reservacion.objects.filter(estado=estadoReservacion)}
    print cntx
    return render_to_response('factura/crear.html', cntx, context_instance=RequestContext(request))


def guardarFactura(request):
    print "ENTROOOOO :V :v "
    factura=request.GET['nFactura']
    cedula = request.GET['cedula']
    codigoProducto= request.GET['codigo']
    cantidad = request.GET['cantidad']
    precio = (request.GET['precio'])
    total =request.GET['total']
    listarProductos=Productos.objects.get(id=codigoProducto)
    print listarProductos  
    print "SIGEEEE"
    print cedula
    laHabitacion = Habitacion.objects.get(habitacion=request.GET['Numerohabitacion'])
    print laHabitacion
    unCliente= Cliente.objects.get(cedula=cedula)
    print unCliente
    f = Factura.objects.filter(id=request.GET['nFactura']).count()
    print f
    print str('factura ')+str(EstadosFactura.objects.get(estado='Activo'))
    if f ==0:
        cliReservacion=Reservacion.objects.get(cliente=unCliente,habitacion=laHabitacion,estado=EstadosReservacion.objects.get(estado='Activo'))
        print cliReservacion
        fact = Factura(
            fecha=request.GET['fecha'],
            subtotal=request.GET['subtotal'],
            iva=request.GET['iva'],
            total =request.GET['total'],
            estado= EstadosFactura.objects.get(estado='Activo'),
            reservacion= cliReservacion
            )
        fact.save()

        laHabitacion.estado=EstadosHabitacion.objects.get(estado='Inactivo')
        laHabitacion.save()
        print "la habitacion se inactivo"
        cliReservacion.estado=EstadosReservacion.objects.get(estado='Inactivo')
        cliReservacion.save()
        print "se cambio reservacion"

    idfac=Factura.objects.get(id=factura)
    print (str('id de factura ')+str(idfac))
    
    ser=ServicioCliente.objects.get(habitacion=laHabitacion,producto=listarProductos,cliente=unCliente,estado=EstadosServicio.objects.get(estado='Activo'))
    print ser
    facser=FacturaServicios(servico=ser,factura=idfac)
    facser.save()
    print str("pasooooooooooooo")
    ser.estado=EstadosServicio.objects.get(estado='Inactivo')
    ser.save()
    print "el servicio paso a inactivo"
    print "---fin---"
    return render_to_response('factura/crear.html',context_instance=RequestContext(request))

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
    def get_context_data(self,**kwargs):
        ctx = super(listarFactura, self).get_context_data(**kwargs)
        ctx['listarClientes'] = Cliente.objects.all()
        ctx['listarFacturas'] = Factura.objects.order_by("id")
        ctx['listarReservacion'] = Reservacion.objects.all()
        return ctx

class buscarFactura(TemplateView):
    def get(self,request,*args,**kwargs):
        buscar = request.GET.get('nombre')
        print buscar

        clie=Cliente.objects.filter(cedula__icontains=buscar)
        print clie

        reser=Reservacion.objects.filter(cliente__icontains=clie)
        print reser


        factu = Factura.objects.filter(Q(reservacion__icontains=reser)|Q(id__icontains=buscar)).order_by("id")
        print factu
        data = serializers.serialize('json',factu,fields=('fecha','subtotal','iva','total','estado','reservacion'))
        return HttpResponse(data,content_type='application/json')


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

def guardarUnaFactura(request):
    print "ENTROOOOO :V :v "
    cedula = request.GET['cedula']
    total =request.GET['total']
    numero=request.GET['Numerohabitacion']
    print "SIGEEEE"
    print cedula
    laHabitacion = Habitacion.objects.get(habitacion=numero)
    print laHabitacion
    unCliente= Cliente.objects.get(cedula=cedula)
    print unCliente
    cliReservacion=Reservacion.objects.get(cliente=unCliente,habitacion=laHabitacion,estado=EstadosReservacion.objects.get(estado='Activo'))
    print " pasoooo id reservacion"
    print cliReservacion
    print str(unCliente.id)+" "+str(unCliente.cedula)+" "+str(unCliente.nombre)
    f = Factura.objects.filter(id=request.GET['nFactura']).count()
    print request.GET['nFactura']
    print f
    print str('factura ')+str(EstadosFactura.objects.get(estado='Activo'))
    if f ==0:
        fact = Factura(
            fecha=request.GET['fecha'],
            subtotal=request.GET['subtotal'],
            iva=request.GET['iva'],
            total =request.GET['total'],
            estado= EstadosFactura.objects.get(estado='Activo'),
            reservacion= cliReservacion
            )
        fact.save()
    print str("pasooooooooooooo")
    
    laHabitacion.estado=EstadosHabitacion.objects.get(estado='Inactivo')
    laHabitacion.save()
    print (str(laHabitacion)+"paso a inactiva")

    cliReservacion.estado=EstadosReservacion.objects.get(estado='Inactivo')
    cliReservacion.save()
    print ("la reservacion se inactivo")
    print "-----fin---"

    return render_to_response('factura/crear.html',context_instance=RequestContext(request))

