from django.shortcuts import render
from django.shortcuts import redirect


from django.http import HttpResponse
from apps.intermediario.models import Intermediario
# Create your views here.

def index(request):
    return render(request, 'intermediario/index.html')

