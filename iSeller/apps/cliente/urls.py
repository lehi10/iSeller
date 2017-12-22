from django.conf.urls import url, include
from apps.cliente.views import index, perfilCliente, carritoCliente, pedidosCliente, editarInformacion_view,listaDeseos


urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilCliente,name='perfil'),
    url(r'^carrito$',carritoCliente,name='carrito'),
    url(r'^pedidos$',pedidosCliente, name='pedidos'),
    url(r'^editarInf/(?P<id_user>.*)$',editarInformacion_view, name='editarInf'),
    url(r'^deseos$',listaDeseos, name='deseos'),
]