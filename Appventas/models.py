from django.db import models

# Create your models here.
from django.db import models
idB=0

# Create your models here.
class bicicletas(models.Model):
    id=models.BigAutoField(primary_key=True)    
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    rodado = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.id,self.marca, self.modelo,self.rodado,self.color,self.precio}"


class repuestos(models.Model):
    id=models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.id,self.tipo,self.marca, self.modelo,self.fabricante,self.precio}"
    

class indumentaria(models.Model):
    id=models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.id,self.tipo,self.marca, self.modelo,self.talle,self.precio}"