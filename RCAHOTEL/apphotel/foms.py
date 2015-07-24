from django import froms

class Formulario(forms.Form):
	nombre=forms.CharField(max_Length=100)
	mensaje=forms.CharField()
	mail=forms.EmailField()
	