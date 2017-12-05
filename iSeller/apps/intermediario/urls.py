from django.conf.urls import url, include
from apps.intermediario.views import index

urlpatterns =[ 
    url(r'^$',index, name='index'),

]