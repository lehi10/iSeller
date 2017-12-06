from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from apps.dashboard.models import Oferta
from apps.proveedor.models import Producto
from apps.proveedor.models import Categoria

def index(request):
    return render(request,'index.html')


def tienda(request):
    return render(request,'tienda/index.html')

def contenido_view(request):
	print("gerererer")
	categorias=Categoria.objects.all()
	ofertas = Oferta.objects.select_related()
	contexto={'mis_categorias': categorias, 'ofert_list' : ofertas}
	for x in categorias:
		print("--->",x.nombre)
	return render(request,'index.html',contexto)

"""
class ofertalist(ListView):
<<<<<<< HEAD
    model = ofertaModel
    queryset = Oferta.objects.select_related()
    template_name = 'index.html'

class productolist(ListView):
    model = Producto
    template_name = 'index.html'
=======
	print("ie")
	queryset = Oferta.objects.select_related()
	template_name = 'index.html'
"""
>>>>>>> BackEnd
