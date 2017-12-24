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
	if 'isLogin' in request.session  and request.session['isLogin']:
		idUsuario = request.session['permisos']
		if(idUsuario=="intermediario"):
			return index_intermediario(request)
		if(idUsuario=='proveedor'):
			return index_proveedor(request)
		if(idUsuario=='cliente'):
			return index_cliente(request)	
	else:
		keywords=''
		categoria=''
		if 'categoria' in request.GET and  request.GET['categoria'] != "" :	
			categoria= request.GET['categoria']
			ofertas = Producto.objects.filter(categoria__icontains = categoria ) ## CAMBIAR DE PRODUCTOS A OFERTAS Y PROMOCIONES
		
		else:
			if 'query' in request.GET and  request.GET['query'] != "" :	
				keywords= request.GET['query']
				ofertas = Producto.objects.filter(nombre__icontains = keywords ) ## CAMBIAR DE PRODUCTOS A OFERTAS Y PROMOCIONES
			else:
				ofertas = Producto.objects.select_related() ## CAMBIAR DE PRODUCTOS A OFERTAS Y PROMOCIONES
			
		categorias=Categoria.objects.all()
		contexto={'mis_categorias': categorias, 'ofert_list' : ofertas}
		return render(request,'index.html',contexto)

def detallesItem(request):
	id= request.GET['id']
	item =Producto.objects.filter(idProducto=id).all()
	item_set={'detalles' : item}
	return render(request,'tienda/item.html',item_set)