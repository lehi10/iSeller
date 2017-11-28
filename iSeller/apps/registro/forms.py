from django import forms
from apps.registro.models import Persona


class RegistroForm(forms.ModelForm):

	class Meta:
		model = Persona

		fields = [
			'usuario',
			'password',
			'nombres',
			'apellidos',
			'sexo',
			'fecha_nac',
			'id_doc',
			'permisos',
			'email',
			'telf',
			'domicilio',
		]
		labels = {
			'usuario' : 'Usuario',
			'password': 'Password',
			'nombres' :'Nombres',
			'apellidos': 'Apellidos',
			'sexo' : 'Sexo',
			'fecha_nac': 'Fecha de Nacimiento',
			'id_doc':'Documento de Identidad',
			'permisos': 'Permisos',
			'email': 'Email',
			'telf': 'Teléfono',
			'domicilio': 'Domicilio',	
		}
		widgets = {
			'usuario':forms.TextInput(attrs={'class':'form-control'}),
			'password':forms.TextInput(attrs={'class': 'form-control','type':'password'}),
			'nombres':forms.TextInput(attrs={'class': 'form-control'}),
			'apellidos':forms.TextInput(attrs={'class': 'form-control'}),
			'sexo':forms.TextInput(attrs={'class': 'form-control'}),
			'fecha_nac':forms.DateInput(attrs={'class': 'form-control','type':'date'}),
			'id_doc':forms.TextInput(attrs={'class': 'form-control'}),
			'permisos':forms.TextInput(attrs={'class': 'form-control'}),
			'email':forms.TextInput(attrs={'class': 'form-control'}),
			'telf':forms.TextInput(attrs={'class': 'form-control'}),
			'domicilio':forms.TextInput(attrs={'class': 'form-control'}),
		}

class LoginForm(forms.Form):
	username = forms.CharField( widget=forms.TextInput,required=True)
	password = forms.CharField(	widget=forms.TextInput, required=True)


