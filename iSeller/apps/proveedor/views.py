from django.shortcuts import render, redirect
from django.views.generic import ListView
from apps.proveedor.models import Producto, Proveedor
from apps.registro.models import Persona
from apps.tienda.views import error404
from apps.proveedor.forms import RegistroProductosForm

from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'proveedor/index.html')


def perfilProveedor(request):
	## VALIDACION PARA SABER SI EL USUARIO HA SIDO LOGEADO Y SI TIENE PERMISOS PARA ACCEDER
	if request.session.get('isLogin') != True or request.session.get('permisos') != 'proveedor':
		return error404(request);
	## Se envian los datos necesarios a la vista del perfil del proveedor
	idUsuario = request.session.get('id_user')
	usuario = Proveedor.objects.filter(idUsuario=idUsuario)
	contexto= {'mi_usuario':usuario , 'id_user':idUsuario}
	return render(request,'proveedor/perfil.html',contexto)     

"""
    Vista registro Producto 
"""
def registroProducto_view(request):
    error = request.GET.get('err',False)
    if request.method == 'POST':
        
        form_producto = RegistroProductosForm(request.POST or None, request.FILES)
        print("-------------")
        if form_producto.is_valid():
            print("es valido")
            datosProducto = form_producto.save(commit=False)
            idProveedor = Proveedor.objects.filter(idUsuario = request.session['id_user']).values()[0]['idProveedor']
            datosProducto.idProveedor_id = idProveedor
            datosProducto.save()
            
            return redirect('/proveedor/regProducto')
    else:
        form_producto = RegistroProductosForm()
    return render(request,'proveedor/regProducto.html', {'form_producto':form_producto ,'error' : error} )

 
