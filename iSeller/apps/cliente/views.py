from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from apps.tienda.views import error404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from django.http import HttpResponse
from apps.registro.models import Persona
from apps.registro.forms import RegistroForm, RegistroUsuarioForm
from apps.cliente.models import Cliente, Pedidos
from apps.cliente.forms import CrearPedidoForm
from django.contrib import auth


from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'cliente/index.html')


def perfilCliente(request):
    ## VALIDACION PARA SABER SI EL USUARIO HA SIDO LOGEADO Y SI TIENE PERMISOS PARA ACCEDER
	if request.session.get('isLogin') != True or request.session.get('permisos') != 'cliente':
		return error404(request);
	idUsuario = request.session.get('id_user')
	usuario = Persona.objects.filter(idUsuario_id=idUsuario)
	contexto= {'mi_usuario':usuario , 'id_user':idUsuario}
	return render(request,'cliente/perfil.html',contexto)   

#muestra la interfaz de los pedidos del cliente
def pedidosCliente(request):
	#obtenemos el id de la persona usando el id cliente
	#IDpersona = Persona.objects.get(idUsuario_id =request.session['id_user'])
	idUsuario = request.session.get('id_user')
	usuario = request.session.get('usuario')
	clienteComoPersona = Persona.objects.get(idUsuario_id=idUsuario)
	IDcliente = Cliente.objects.get(persona_id =clienteComoPersona.idPersona)
	lista_pedidos = Pedidos.objects.filter(idCliente_id=IDcliente.idCliente)
	#obtenemos la fecha actual 
	if request.method == 'POST':
		form_pedido = CrearPedidoForm(request.POST or None)
		if form_pedido.is_valid():
			#obtenemos lod datos llenados desde el formulario
			datos_pedido = form_pedido.save(commit=False)
			#E llenamos los campos que no se llenaron desde formulario
			datos_pedido.fecha_pedido = datetime.now()
			#Guardamos el id del cliente actual en el pedido realizado
			datos_pedido.idCliente_id=IDcliente.idCliente
			datos_pedido.save()
	else: 
		form_pedido = CrearPedidoForm()
	contexto= {'form_pedido':form_pedido,'lista_pedidos':lista_pedidos,'mi_usuario':usuario , 'id_user':idUsuario}
	return render(request, 'cliente/pedidos.html', contexto)


def carritoCliente(request):
    return render(request, 'cliente/carrito.html')

#Editamos informacion del usuario
def editarInformacion_view(request, id_user):
	usuario = Persona.objects.get(idPersona = id_user)
	print(usuario.nombres)
	if request.method =="POST":
		form = RegistroForm(request.POST or None)
		if form.is_valid():
			usuario.nombres = form.cleaned_data['nombres']
			usuario.apellidos = form.cleaned_data['apellidos']
			usuario.sexo = form.cleaned_data['sexo']
			usuario.fecha_nac = form.cleaned_data['fecha_nac']
			usuario.id_doc = form.cleaned_data['id_doc']
			usuario.telf = form.cleaned_data['telf']
			usuario.domicilio = form.cleaned_data['domicilio']
			usuario.save()
			return redirect('/cliente/perfil')
		#return render(request,'cliente/perfil.html',{'mi_usuario':usuario})   
	if request.method == "GET":
		form_editar = RegistroForm(initial={
			'nombres': usuario.nombres,
			'apellidos': usuario.apellidos,
			'sexo':usuario.sexo,
			'fecha_nac': usuario.fecha_nac,
			'id_doc': usuario.id_doc,
			'telf':usuario.id_doc,
			'domicilio':usuario.domicilio,
			})
		contexto = {'form_editar':form_editar, 'usuario':usuario}
		return render(request,'cliente/editarInf.html',contexto)

def listaDeseos(request):
	return render(request,'cliente/lista_deseos.html')


def pagos(request):
    	return render(request,'cliente/pagos.html')



