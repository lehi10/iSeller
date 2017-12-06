from django.conf.urls import url, include

from apps.dashboard.views import *
from apps.dashboard.views import traer_categoria

urlpatterns = [
	url(r'^$', traer_categoria), 
    url(r'^$', ofertalist.as_view()),   
    
    url(r'^tienda$', tienda),
    
]

