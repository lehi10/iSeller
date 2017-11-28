from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')


def tienda(request):
    return render(request,'tienda/index.html')