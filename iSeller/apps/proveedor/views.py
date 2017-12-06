from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from apps.proveedor.models import Producto

from django.http import HttpResponse


# Create your views here.

def index(request):
	print("hii")
	return render(request, 'proveedor/index.html')


