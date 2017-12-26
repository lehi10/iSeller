from django.conf.urls import url, include
<<<<<<< HEAD
from apps.cliente.views import index,pagos, perfilCliente, carritoCliente, pedidosCliente, editarInformacion_view,listaDeseos
=======
from apps.cliente.views import pagos, perfilCliente, carritoCliente, editarInformacion_view,listaDeseos
from apps.cliente.views import index,crearPedido,editarPedido,eliminarPedido,mostrarPedidos

>>>>>>> FrontEnd


urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilCliente,name='perfil'),
    url(r'^carrito$',carritoCliente,name='carrito'),
    url(r'^pedidos$',pedidosCliente, name='pedidos'),
    url(r'^editarInf/(?P<id_user>.*)$',editarInformacion_view, name='editarInf'),
    url(r'^deseos$',listaDeseos, name='deseos'),
    url(r'^pagos$',pagos, name='pagos'),
]