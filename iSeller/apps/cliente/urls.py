from django.conf.urls import url, include
from apps.cliente.views import index

urlpatterns =[ 
    url(r'^$',index),
]