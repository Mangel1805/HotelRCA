from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import TemplateView,FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.template import Context
# Create your views here.


class Registrarse(FormView):
    template_name = 'inicio/registrarse.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        perfil=Perfiles()
     
        perfil.usuario = user
        perfil.telefono = form.cleaned_data['telefono']
        perfil.correo=form.cleaned_data['correo']
        perfil.direccion=form.cleaned_data['direccion']
        print str(form.cleaned_data['cargo'])
        tipo=TipoCargo.objects.get(id=form.cleaned_data['cargo'])
        print tipo
        perfil.cargo=TipoCargo.objects.get(id=form.cleaned_data['cargo'])
        perfil.save()
        return super(Registrarse, self).form_valid(form)
    




#def inicio(request):
 #   return render_to_response('inicio/login.html')
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