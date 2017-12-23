from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from apps.dashboard.models import Oferta
from apps.proveedor.models import Producto
from apps.proveedor.models import Categoria
from apps.intermediario.views import index as index_intermediario
from apps.proveedor.views import index as index_proveedor
from apps.cliente.views import index as index_cliente

def index2(request):
    return render(request,'index.html')


def tienda(request):
    return render(request,'tienda/index.html')

def contenido_view(request):
	if(request.session['isLogin']):
		idUsuario = request.session['permisos']
		if(idUsuario=="intermediario"):
			print("hi")
			return index_intermediario(request)
		if(idUsuario=='proveedor'):
			return index_proveedor(request)
		if(idUsuario=='cliente'):
			return index_cliente(request)
		print("->>>>>>",idUsuario)
	else:
		categorias=Categoria.objects.all()
		ofertas = Producto.objects.select_related() ## CAMBIAR DE PRODUCTOS A OFERTAS Y PROMOCIONES
		contexto={'mis_categorias': categorias, 'ofert_list' : ofertas}
		for x in categorias:
			print("--->",x.nombre)
		return render(request,'index.html',contexto)

def detallesItem(request):
	id= request.GET['id']
	item =Producto.objects.filter(idProducto=id).all()
	item_set={'detalles' : item}
	return render(request,'tienda/item.html',item_set)