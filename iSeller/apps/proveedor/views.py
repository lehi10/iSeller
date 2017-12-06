from django.shortcuts import render
from django.shortcuts import redirect


from django.http import HttpResponse
from apps.proveedor.models import Proveedor
# Create your views here.

def index(request):
    return render(request, 'proveedor/index.html')

