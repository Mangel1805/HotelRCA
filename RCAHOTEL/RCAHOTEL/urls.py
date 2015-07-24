"""RCAHOTEL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from apphotel.views import inicio
from apphotel.views import postt
admin.autodiscover()

urlpatterns = patterns('',

	#url(r'^$', include('apphotel.urls')),
	#url(r'^RCAHOTEL/apphotel/', include('apphotel.urls')),
    
    #url(r'^$', postt),
    url(r'^$', inicio),
    url(r'^inicio/$', 'apphotel.views.inicio'),
    url(r'^nosotros/$', 'apphotel.views.nosotros'),
    url(r'^galeria/$', 'apphotel.views.galeria'),
    url(r'^servicios/$', 'apphotel.views.servicios'),
    url(r'^contactenos/$', 'apphotel.views.contactenos'),
    url(r'^sistema/$', 'apphotel.views.sistema'),
    url(r'^login/$', 'apphotel.views.login'),
    url(r'^registrarse/$', 'apphotel.views.registrarse'),
    url(r'^reservacion/$', 'apphotel.views.reservacion'),
    url(r'^imprimir/$', 'apphotel.views.imprimir'),



    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

    url(r'^contacto/$', 'apphotel.views.contacto', name='contacto'),
    url(r'^gracias/$', 'apphotel.views.gracias', name='gracias'),

    url(r'^RCAHOTEL/admin/', include(admin.site.urls)),
)
