from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.core.exceptions import ObjectdoesNotExist
# Create your views here.
from apps.registro.forms import RegistroForm
from apps.registro.forms import LoginForm
from apps.registro.models import Persona
from apps.cliente.views import index, perfilCliente


"""
    Función para iniciar sesión
"""
def iniciarSesion( request, user):
    request.session['id_user'] = user.values()[0]['idPersona']
    request.session['nombres'] = user.values()[0]['nombres']
    request.session['apellidos'] = user.values()[0]['apellidos']
    request.session['permisos'] = user.values()[0]['permisos']
    request.session['isLogin']=True
    
def permisosUsuario(request):
    return request.session['permisos']


"""
    Funcion para cerrar Sesión
"""
def cerrarSesion(request ):
    del request.session['id_user']
    del request.session['nombres']
    del request.session['apellidos']
    del request.session['permisos']
    request.session['isLogin']=False

""""
    Permite el logeo por nombre de usuario o correo
"""
def login_corre_or_username(nameus, clave):
    user = Persona.objects.filter(usuario=nameus,password=clave)
    if user.exists():  
        return user
    else:
        user = Persona.objects.filter(email=nameus,password=clave)
        return user


"""
    Vista de Registro
"""
def registro_view(request):
    
    error = request.GET.get('err',False)
    if request.method == 'POST':
        form = RegistroForm(request.POST or None)
        if form.is_valid():
            form.save()
            name_us= form.cleaned_data.get("usuario")
            user = Persona.objects.filter(usuario=name_us)
            iniciarSesion(request,user)                     ## INICIAR SESSIÓN
            form.save()
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request,'registro/index.html', {'form':form , 'error' : error} )


"""
    Función login, que recibe por POST los parametros de usuario y contraseña
"""
def login_view(request):
    if request.method == 'POST':
        form_login=LoginForm(request.POST or None)
        if form_login.is_valid():
            name_us = form_login.cleaned_data.get("username")
            password_us = form_login.cleaned_data.get("password")
            user = login_corre_or_username(name_us,password_us)
            permisos = 'cliente'
            if user.exists():    
                iniciarSesion(request,user)                  ## INICIAR SESION
                permisos = permisosUsuario(request)
<<<<<<< Updated upstream
            return redirect('/'+permisos+'/perfil')        
=======
                print("permisos:",permisos)
                return redirect('/'+permisos+'/perfil')        
>>>>>>> Stashed changes
    form_login = LoginForm()
    return redirect('/registro?err=log')
    

"""
    Vista cerrar sesión 
"""
def logout_view(request):
    if request.session['isLogin'] == True:
        cerrarSesion(request)                                ## CERRAR SESION
    return redirect('/')
