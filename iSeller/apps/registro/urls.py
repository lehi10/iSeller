from django.conf.urls import url, include

from apps.registro.views import  registro_view
from apps.registro.views import  login_view
urlpatterns = [
		url(r'^$', registro_view),
        url(r'^login$', login_view),
]

 