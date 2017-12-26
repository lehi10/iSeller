from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from apps.registro.models import Persona
# Create your views here.

def index(request):
    return render(request, 'intermediario/index.html')

def perfilIntermediario(request):
    if request.session.get('isLogin') ==True :
        if request.session.get('permisos') == 'intermediario':
            user_id_session =request.session.get('id_user')
            cliente = Persona.objects.filter(idPersona=user_id_session)
            contexto= {'mi_cliente':cliente , 'id_user':user_id_session }
            return render(request,'intermediario/perfil.html',contexto) 
    return redirect('/')