from django.db import models
from apps.proveedor.models import Producto

class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    nombre_oferta = models.CharField(max_length=50)
    descripcion_oferta = models.CharField(max_length=300)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)

