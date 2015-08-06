from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404

# Create your views here.
def inicio(request):
    return render_to_response('inicio/index.html')
#registro de cliente


def nosotros(request):
    return render_to_response('inicio/nosotros.html')

def galeria(request):
    return render_to_response('inicio/galeria.html')

def servicios(request):
    return render_to_response('inicio/servicios.html')

def contactenos(request):
    return render_to_response('inicio/contactenos.html')

def sistema(request):
    return render_to_response('inicio/sistema.html')

def login(request):
    return render_to_response('inicio/login_solo.html')

def registrarse(request):
    return render_to_response('inicio/registro.html')

def reservacion(request):
    return render_to_response('inicio/reservaciones.html')

def imprimir(request):
    return render_to_response('inicio/imprimir.html')