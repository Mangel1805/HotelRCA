# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.sistema.models import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.http import HttpResponse
from django.core import serializers	
from django.db.models import Q

from io import BytesIO
from django.views.generic import ListView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table


class index(TemplateView):
	template_name='inicio/index.html'


class crearCliente(CreateView):
    model=Cliente
    template_name='cliente/crear.html'
    success_url=reverse_lazy('listarCliente')
    def get_context_data(self,**kwargs):
        ctx = super(crearCliente, self).get_context_data(**kwargs)
        ctx['listarCliente'] = Cliente.objects.order_by("id")
        return ctx

class editarCliente(UpdateView):
	model=Cliente
	template_name='cliente/editar.html'
	success_url=reverse_lazy('listarCliente')

class eliminarCliente(DeleteView):
	model=Cliente
	context_object_name="cliente"
	template_name='cliente/eliminar.html'
	success_url=reverse_lazy('listarCliente')

class listarCliente(ListView):
    model=Cliente
    template_name='cliente/listar.html'
    context_object_name='clientes'
    def get_context_data(self,**kwargs):
        ctx = super(listarCliente, self).get_context_data(**kwargs)
        ctx['listarCliente'] = Cliente.objects.order_by("id")
        ctx['listarCiudad'] = Ciudad.objects.all()
        return ctx
           
class buscarCliente(TemplateView):
    def get(self,request,*args,**kwargs):
        buscar = request.GET.get('nombre')
        print buscar
        cliente = Cliente.objects.filter(Q(cedula__icontains =buscar)|Q(nombre__icontains=buscar)|Q(apellido__icontains=buscar)).order_by("id")
        print cliente
        data = serializers.serialize('json',cliente,fields=('id','cedula','nombre','apellido','telefono','direccion','email','ocupacion','estado','ciudad'))
        return HttpResponse(data,content_type='application/json')


def generar_pdf(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"  # llamado clientes
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
    clientes = []
    estilo = getSampleStyleSheet()
    Encabezado = Paragraph("Listado de Clientes Actuales", estilo['Heading1'])
    clientes.append(Encabezado)
    titulos = ('Cedula','Nombre','Apellido','Teléfono', 'Dirección','Email', 'Ocupacion','Estado','Ciudad' )
    consulta = [(cli.cedula,cli.nombre,cli.apellido,cli.telefono,cli.direccion,cli.email,cli.ocupacion,cli.estado,cli.ciudad) for cli in Cliente.objects.all()]
    print consulta

    tabla = Table([titulos] + consulta)
    tabla.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (8, -1), 1, colors.black),#cuadricula
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),#lineadebajo del titulos
            ('BACKGROUND', (0, 0), (-1, 0), colors.brown)
            
        ]
    ))
    clientes.append(tabla)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response