# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from apphotel.models import HotelrcaPost
from datetime import date
import datetime


# Create your views here.
def postt(request):
	posts=HotelrcaPost.objects.all()
	mi_template=loader.get_template("postt.html")
	mi_contexto=Context({'posts':posts})
	return HttpResponse(mi_template.render(mi_contexto))

#def postt(request):
    #return render_to_response('postt.html')
def contacto(request):
    if request.method=='POST':
        form=Formulario(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/RCAHOTEL/apphotel/gracias/')
    else:
        form= Formulario()
    return render(request, 'contacto.html',{
        'form':form,
    })

def gracias(request):
    html='<html><body>"Gracias por enviarnos su comentario..."</body></html>'
    return HttpResponse(html)



def inicio(request):
    return render_to_response('index.html')
#registro de cliente


def nosotros(request):
    return render_to_response('nosotros.html')

def galeria(request):
    return render_to_response('galeria.html')

def servicios(request):
    return render_to_response('servicios.html')

def contactenos(request):
    return render_to_response('contactenos.html')

def sistema(request):
    return render_to_response('sistema.html')

def login(request):
    return render_to_response('login_solo.html')

def registrarse(request):
    return render_to_response('registro.html')

def reservacion(request):
    return render_to_response('reservaciones.html')

def imprimir(request):
    return render_to_response('imprimir.html')