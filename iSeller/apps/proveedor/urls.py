from django.conf.urls import url, include
from apps.proveedor.views import index, perfilProveedor, registroProducto_view

urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilProveedor,name='perfil'),
    url(r'^regProducto$',registroProducto_view,name='Registrar Producto'),
    
]