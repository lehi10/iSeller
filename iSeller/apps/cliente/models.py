from django.db import models

from apps.registro.models import Persona
# Create your models here.

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    persona = models.OneToOneField(Persona,null=False,blank=False, on_delete=models.CASCADE)
    ##Falta id carrito de compras 



