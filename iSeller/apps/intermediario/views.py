from django.shortcuts import render
from django.shortcuts import redirect
from apps.tienda.views import error404


from django.http import HttpResponse
from apps.registro.models import Persona
from apps.cliente.models import Pedidos
# Create your views here.

def index(request):
	pedidos=Pedidos.objects.all()
	contexto={'mis_pedidos':pedidos}
	return render(request, 'intermediario/index.html',contexto)


def perfilIntermediario(request):
    ## VALIDACION PARA SABER SI EL USUARIO HA SIDO LOGEADO Y SI TIENE PERMISOS PARA ACCEDER
	if request.session.get('isLogin') != True and request.session.get('permisos') != 'intermediario':
		return error404(request);
	idUsuario = request.session.get('id_user')
	usuario = Persona.objects.filter(idUsuario=idUsuario)
	contexto= {'mi_usuario':usuario , 'id_user':idUsuario}
	return render(request,'intermediario/perfil.html',contexto)     

