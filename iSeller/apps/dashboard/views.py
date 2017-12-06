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

def detallesItem(request):
	id= request.GET['id']
	item =Producto.objects.filter(idProducto=id).all()
	item_set={'detalles' : item}
	return render(request,'tienda/item.html',item_set)
