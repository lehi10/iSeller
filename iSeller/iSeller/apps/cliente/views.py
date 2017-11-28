from django.shortcuts import render
from django.http import HttpResponse



from apps.cliente.models  import Cliente
from apps.registro.models  import Persona

# Create your views here.



def index(request):
    return render(request, 'cliente/index.html')

  


    
