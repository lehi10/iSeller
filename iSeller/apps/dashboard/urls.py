from django.conf.urls import url, include

from apps.dashboard.views import *
from apps.dashboard.views import contenido_view

urlpatterns = [
	url(r'^$', contenido_view), 
    ##url(r'^$', ofertalist.as_view()),   
    url(r'^tienda$', tienda),
    
]

