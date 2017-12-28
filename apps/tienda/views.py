from django.shortcuts import render
from django.http import HttpResponse
from apps.proveedor.models import Categoria

# Create your views here.

def index(request):
    return render(request, 'tienda/404.html')

def error404(request):
    return render(request, 'tienda/404.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def categoriasInput(request):    

    p = Categoria(nombre='moda')
    p.save()
    p = Categoria(nombre='celulares')
    p.save()
    p = Categoria(nombre='hogar')
    p.save()
    p = Categoria(nombre='deportes')
    p.save()
    p = Categoria(nombre='jugueteria')
    p.save()
    p = Categoria(nombre='computo')
    p.save()
    
    
    print('here')
    return render(request,'/index.html')
    