from django.shortcuts import render
from django.shortcuts import redirect
from apps.tienda.views import error404

from django.http import HttpResponse
from apps.registro.models import Persona
# Create your views here.

def index(request):
    return render(request, 'cliente/index.html')





def perfilCliente(request):
    ## VALIDACION PARA SABER SI EL USUARIO HA SIDO LOGEADO Y SI TIENE PERMISOS PARA ACCEDER
	if request.session.get('isLogin') != True or request.session.get('permisos') != 'cliente':
		return error404(request);
	idUsuario = request.session.get('id_user')
	usuario = Persona.objects.filter(idPersona=idUsuario)
	contexto= {'mi_usuario':usuario , 'id_user':idUsuario}
	return render(request,'cliente/perfil.html',contexto)     



def carritoCliente(request):
    return render(request, 'cliente/carrito.html')

    