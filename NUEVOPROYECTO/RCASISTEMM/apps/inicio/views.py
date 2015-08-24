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

class nosotros(TemplateView):
    template_name='inicio/nosotros.html'

class galeria(TemplateView):
    template_name='inicio/galeria.html'

class servicios(TemplateView):
    template_name='inicio/servicios.html'

class contactenos(TemplateView):
    template_name='inicio/contactenos.html'

class sistema(TemplateView):
    template_name='inicio/sistema.html'

class galeria(TemplateView):
    template_name='inicio/galeria.html'


class detalles(TemplateView):
    template_name='inicio/detalles.html'