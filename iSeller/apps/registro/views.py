from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.core.exceptions import ObjectdoesNotExist
# Create your views here.
from apps.registro.forms import RegistroForm
from apps.registro.forms import LoginForm
from apps.registro.models import Persona
from apps.cliente.views import index, perfilCliente




def registro_view(request):
	if request.method == 'POST':
		#PersonaForm es mi clase creada en archivo forms.py
		form = RegistroForm(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('/')
	else:
		form = RegistroForm()
	return render(request,'registro/index.html', {'form':form } )


def login_view(request):
    if request.method == 'POST':
        form_login=LoginForm(request.POST)
        if form_login.is_valid():
            datos = form_login.cleaned_data
            name_us = datos.get("username")
            password_us = datos.get("password")
            user = Persona.objects.filter(usuario=name_us,password=password_us)
            if user.exists():    
                request.session['id_user'] = user.values()[0]['idPersona']
                request.session['nombres'] = user.values()[0]['nombres']
                request.session['apellidos'] = user.values()[0]['apellidos']
                request.session['isLogin']=True
                return redirect('/cliente/perfil') 
    else:
        form_login = LoginForm()
        return render(request,'registro/login.html',{'form_login':form_login})
    
def logout_view(request):
    if request.session['isLogin'] == True:
        del request.session['id_user']
        del request.session['nombres']
        del request.session['apellidos']
        request.session['isLogin']=False
    return redirect('/')
