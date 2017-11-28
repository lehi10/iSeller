from django.shortcuts import render

from django.http import HttpResponse
from apps.registro.models import Persona
# Create your views here.

def index(request):
    return render(request, 'cliente/index.html')



def perfilCliente(request):
    print("asdasdasd")
    user_id_session = '123'##request.session.get('id_user')
    cliente = Persona.objects.all()    
    contexto= {'mi_cliente':cliente , 'id_user':user_id_session }
    return render(request,'cliente/perfil.html',contexto) 