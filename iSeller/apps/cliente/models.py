from django.db import models


from apps.registro.models import Persona
from apps.proveedor.models import Producto
# Create your models here.

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    persona = models.OneToOneField(Persona,null=False,blank=False, on_delete=models.CASCADE)
    ##Falta id carrito de compras 

#tabla de lista de pedidos de cada cliente
class Pedidos(models.Model):
	idPedido = models.AutoField(primary_key=True)
	idCliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
	nombre = models.CharField(blank=True, max_length=100)
	descripcion = models.TextField(null=False, max_length=500)
	categoria = models.CharField(max_length=10)
	fecha_pedido = models.DateField()

#tabla de lista de deseos
class Lista_deseos(models.Model):
	idProducto = models.ForeignKey(Producto,null=False,blank=False,on_delete=models.CASCADE)
	idCliente = models.ForeignKey(Persona,null=False,blank=False,on_delete=models.CASCADE)
