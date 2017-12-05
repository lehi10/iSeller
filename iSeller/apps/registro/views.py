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
        form = RegistroForm(request.POST or None)
        if form.is_valid():
            form.save()
            name_us= form.cleaned_data.get("usuario")
            user = Persona.objects.filter(usuario=name_us)
            request.session['id_user'] = user.values()[0]['idPersona']
            request.session['nombres'] = user.values()[0]['nombres']
            request.session['apellidos'] = user.values()[0]['apellidos']
            request.session['isLogin']=True
            form.save()
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request,'registro/index.html', {'form':form } )

#permite el logeo por nombre de usuario o correo
def login_corre_or_username(nameus, clave):
    user = Persona.objects.filter(usuario=nameus,password=clave)
    if user.exists():  
        return user
    else:
        user = Persona.objects.filter(email=nameus,password=clave)
        return user


def login_view(request):
    if request.method == 'POST':
        form_login=LoginForm(request.POST or None)
        if form_login.is_valid():
            name_us = form_login.cleaned_data.get("username")
            password_us = form_login.cleaned_data.get("password")
            user = login_corre_or_username(name_us,password_us)
            if user.exists():    
                request.session['id_user'] = user.values()[0]['idPersona']
                request.session['nombres'] = user.values()[0]['nombres']
                request.session['apellidos'] = user.values()[0]['apellidos']
                request.session['isLogin']=True
<<<<<<< Updated upstream
            return redirect('/')
=======
            return redirect('/cliente/perfil')
    
>>>>>>> Stashed changes
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
