from django.shortcuts import render, redirect
from django.views.generic import ListView
from apps.proveedor.models import Producto
from apps.registro.models import Persona
from apps.tienda.views import error404


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
	usuario = Persona.objects.filter(idPersona=idUsuario)
	contexto= {'mi_usuario':usuario , 'id_user':idUsuario}
	return render(request,'proveedor/perfil.html',contexto)     



