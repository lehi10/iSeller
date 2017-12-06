from django.db import models


class Intermediario(models.Model):
    idIntermediario = models.AutoField(primary_key=True, null=False,blank=False)
    idPersona = models.OneToOneField(Persona,null=False,blank=False, on_delete=models.CASCADE)
    calificacion = models.IntegerField(default=0)
    
