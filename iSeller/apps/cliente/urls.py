from django.conf.urls import url, include
from apps.cliente.views import index, perfilCliente, carritoCliente

urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilCliente,name='perfil'),
    url(r'^carrito$',carritoCliente,name='carrito'),
]