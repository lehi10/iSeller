from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from apps.dashboard.models import Oferta
from apps.proveedor.models import Producto

def index(request):
    return render(request,'index.html')


def tienda(request):
    return render(request,'tienda/index.html')

class ofertalist(ListView):
    queryset = Oferta.objects.select_related()
    template_name = 'index.html'