from django.db import models

# Create your models here.

class Producto(models.Model):
    precio = models.IntegerField(default=0)
	costo = models.IntegerField(default=0)
	nombre = models.CharField(max_length=200)
    proveedor = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    codigos = models.IntegerField(default=0)
    especificos = models.CharField(max_length=400)
    fecha_creacion = models.DateTimeField('date published')
    fecha_act = models.DateTimeField('date published')
