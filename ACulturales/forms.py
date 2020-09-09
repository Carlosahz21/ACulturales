from django import forms
from .models import *


# Formulario Parroquia
class ParroquiaForm(forms.ModelForm):
	class Meta:
		model = Parroquia
		fields = [
			"nombre_parroquia", 
			"nombre_presidente",
			"direccion_parroquia", 
			"telefono_parroquia", 
			"correo_parroquia"
			]


# Formulario Categoria
class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = [
			"nombre_categoria"
		]


# Formulario Ambito
class AmbitoForm(forms.ModelForm):
	class Meta:
		model = AmbitoCultural
		fields = [
			"nombre_ambito"
		]


# Formulario Agrupacion
class AgrupacionForm(forms.ModelForm):
	class Meta:
		model = Agrupacion
		fields = '__all__'