from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from apps.registro.forms import PersonaForm
##from apps.registro.models import Persona



def registro_view(request):
	if request.method == 'POST':
		#PersonaForm es mi clase creada en archivo forms.py
		form = PersonaForm(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = PersonaForm()
	return render(request,'registro/index.html', {'form':form } )


def login_view(request):
    return render(request,'registro/login.html')


