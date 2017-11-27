from django.conf.urls import url, include

from apps.dashboard.views import *

urlpatterns = [
    url(r'^$', index),    
    url(r'^tienda$', tienda),    
]
