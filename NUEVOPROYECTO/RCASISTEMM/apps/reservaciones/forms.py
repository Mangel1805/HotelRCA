from django import forms
from django.forms import ModelForm
from apps.sistema.models import Reservacion


class reservacionForm(ModelForm):
	class Meta:
		model=Reservacion
		


