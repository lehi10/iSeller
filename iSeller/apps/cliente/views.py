from django.shortcuts import render

from django.http import HttpResponse
from apps.registro.models import Persona
# Create your views here.

def index(request):
    return render(request, 'cliente/index.html')
def cliente_list(request):
	print ("prueba p papi")
	cliente_ = Persona.objects.all()
	contexto= {'mi_cliente':cliente_}
	print(contexto)
	return render(request,'cliente/cliente_list.html',contexto)
