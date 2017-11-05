from django.db import models

# Create your models here.

class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True)
    usuario = models.CharField(db_index=True , max_length=20)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    fecha_nac = models.DateField()
    id_doc = models.CharField(max_length=10)
    permisos = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    telf = models.CharField(max_length=15)
    domicilio = models.TextField(max_length=15)