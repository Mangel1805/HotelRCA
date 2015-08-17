# -*- coding: utf-8 -*-

from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table


from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from apps.sistema.models import Factura,Cliente,Productos,EstadosFactura,Reservacion,EstadosReservacion,EstadosHabitacion,EstadosProducto,EstadosCliente,Habitacion,ServicioCliente,FacturaServicios
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
#from django.template import Context, Template,RequestContext

class index(TemplateView):
	template_name='inicio/index.html'

def generarVentaFactura(request):
    estadoHabitacion = EstadosHabitacion.objects.get(estado='Activo')
    estadoProducto = EstadosProducto.objects.get(estado='Activo')
    estadoCliente=EstadosCliente.objects.get(estado='Activo')
    estadoReservacion=EstadosCliente.objects.get(estado='Activo')
    print estadoHabitacion
    cntx={'listarHabitacion':Habitacion.objects.filter(estado=estadoHabitacion),'listarclientes':Cliente.objects.filter(estado=estadoCliente), 
          'listarproductos':Productos.objects.filter(estado=estadoProducto), 'nFactura': 1+Factura.objects.count(),
          'listaServicios':ServicioCliente.objects.all(),'listaReservacion':Reservacion.objects.filter(estado=estadoReservacion)}
    print cntx
    return render_to_response('factura/crear.html', cntx, context_instance=RequestContext(request))


def guardarFactura(request):
    print "ENTROOOOO :V :v "
    cedula = request.GET['cedula']

    codigoProducto= request.GET['codigo']
    cantidad = request.GET['cantidad']
    precio = (request.GET['precio'])
    total =request.GET['total']
    print "SIGEEEE"
    print cedula
    elCliente = Cliente.objects.get(cedula=cedula)
    laHabitacion = Habitacion.objects.get(habitacion=request.GET['Numerohabitacion'])

   
    unCliente= Cliente.objects.get(cedula=cedula)
    cliReservacion=Reservacion.objects.get(cliente=elCliente,habitacion=laHabitacion)
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

    
    idfac=Factura.objects.get(id=request.GET['nFactura'])
    print (str('id de factura ')+str(idfac))
    
   
    listarProductos = Productos.objects.get(id=codigoProducto)
    print listarProductos
    ser=ServicioCliente.objects.get(producto=listarProductos,cliente=unCliente)

    facser=FacturaServicios(
         servico=ser,
         factura=idfac
        )
    facser.save()
    print str("pasooooooooooooo")
    
    return render_to_response('factura/crear.html',context_instance=RequestContext(request))

    



def guardarUnaFactura(request):
    print "ENTROOOOO :V :v "
    cedula = request.GET['cedula']


    total =request.GET['total']
    print "SIGEEEE"
    print cedula
  
    laHabitacion = Habitacion.objects.get(habitacion=request.GET['Numerohabitacion'])

   
    unCliente= Cliente.objects.get(cedula=cedula)
    cliReservacion=Reservacion.objects.get(cliente=unCliente,habitacion=laHabitacion)
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