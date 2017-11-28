from django.db import models
from apps.registro.models import Persona


class Intermediario(models.Model):
    idIntermediario = models.AutoField(primary_key=True)
    persona = models.OneToOneField(Persona,null=False,blank=False, on_delete=models.CASCADE)
    