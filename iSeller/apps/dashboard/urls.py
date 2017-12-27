from django.conf.urls import url, include

from apps.dashboard.views import *
from apps.dashboard.views import contenido_view
from apps.dashboard.views import detallesItem
from apps.dashboard.views import notificaciones
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', contenido_view), 
    ##url(r'^$', ofertalist.as_view()),   
    url(r'^categoria$', tienda),
    url(r'^detalles$', detallesItem),
    url(r'^notificaciones$', notificaciones),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

