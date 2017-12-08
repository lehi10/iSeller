from django.conf.urls import url, include
from apps.proveedor.views import index, perfilProveedor

urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilProveedor,name='perfil'),
]