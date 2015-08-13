from django import forms
from django.contrib.auth.forms import UserCreationForm
tiposEmpleados = (
    ('1', 'Recepcionista'),
    ('2', 'Cajero'),
    ('3', 'Bodeguero'),
    ('4', 'Conserje'),
)

class UserForm(UserCreationForm):
	telefono = forms.IntegerField()
	correo = forms.EmailField()
	direccion = forms.CharField()
	cargo=forms.ChoiceField(choices=tiposEmpleados)



# 	CHOICES=[('select1','select 1'),
#          ('select2','select 2')]

# like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())