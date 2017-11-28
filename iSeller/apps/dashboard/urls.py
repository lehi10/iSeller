from django.conf.urls import url, include

from apps.dashboard.views import *


urlpatterns = [
    url(r'^$', ofertalist.as_view()),    
    url(r'^tienda$', tienda),    
    
]

