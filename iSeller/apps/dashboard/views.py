from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from apps.dashboard.models import ofertaModel

def index(request):
    return render(request,'index.html')

def tienda(request):
    return render(request,'tienda/index.html')

class ofertalist(ListView):
    model = ofertaModel
    template_name = 'index.html'
    
