from django.conf.urls import url, include
from apps.intermediario.views import index
from apps.intermediario.views import perfilIntermediario

urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilIntermediario,name='perfil'),

]