from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from apps.proveedor.models import Producto
from apps.registro.models import Persona


from django.http import HttpResponse


# Create your views here.

def index(request):
	print("hii")
	return render(request, 'proveedor/index.html')



def perfilProveedor(request):
    if request.session.get('isLogin') ==True :
    	if request.session.get('permisos') == 'proveedor':
        	user_id_session =request.session.get('id_user')
        	cliente = Persona.objects.filter(idPersona=user_id_session)
        	contexto= {'mi_cliente':cliente , 'id_user':user_id_session }
        	return render(request,'proveedor/perfil.html',contexto) 
    return redirect('/')