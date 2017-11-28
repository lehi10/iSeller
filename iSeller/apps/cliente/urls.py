from django.conf.urls import url, include
from apps.cliente.views import index,cliente_list

urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^listar$',cliente_list,name='cliente_listar'),
]