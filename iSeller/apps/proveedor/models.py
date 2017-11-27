from django.db import models


class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True, null=False,blank=False)
    ruc = models.CharField(db_index=True ,null=False,blank=False, max_length=20)
    razonSocial = models.CharField(db_index=True,null=False,blank=False, max_length=100)
    encargado = models.CharField(null=False,max_length=100)
    categoria = models.CharField(null=True,blank=False,max_length=20)
    telf = models.CharField(null=True,blank=False,max_length=15)
    domicilio = models.TextField(null=False, max_length=100)
    email = models.CharField(null=True,max_length=50)
    info = models.CharField(null=False,max_length=300)
    usuario = models.CharField(blank=False,max_length=50)
    password = models.CharField(max_length=100)    
    calificacion = models.IntegerField(default=0)
    
class Producto(models.Model):
    idProducto =models.AutoField(primary_key=True)
    idProveedor = models.ForeignKey(Proveedor,null=False,blank=False)
    nombre = models.CharField(blank=True,max_length=100)
    medidas = models.CharField(blank=True,max_length=50)
    marca = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    calificacion = models.IntegerField(default=0)
    tags = models.CharField(max_length=50)
    info =models.CharField(max_length=500)