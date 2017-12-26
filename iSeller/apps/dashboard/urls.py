from django.conf.urls import url, include

from apps.dashboard.views import *
from apps.dashboard.views import contenido_view
from apps.dashboard.views import detallesItem

urlpatterns = [
	url(r'^$', contenido_view), 
    ##url(r'^$', ofertalist.as_view()),   
    url(r'^categoria$', tienda),
    url(r'^detalles$', detallesItem),
    
]

