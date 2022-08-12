
from django.db import models

# Create your models here.
from django.db import models



class producto (models.Model):
   #id=models.BigAutoField(primary_key=True)
    precio = models.IntegerField()
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
   

    class Meta:
        abstract = True

# Create your models here.
class bicicletas(producto):
    rodado = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
   
    def __str__(self):
        return f"{self.marca, self.modelo,self.rodado,self.color,self.precio}"


class repuestos(models.Model):#Borre fabricante
    tipo = models.CharField(max_length=30)
   
    def __str__(self):
        return f"{self.tipo,self.marca, self.modelo,self.precio}"
    

class indumentaria(models.Model):
    tipo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    

    def __str__(self):
        return f"{self.tipo,self.marca, self.modelo,self.talle,self.precio}"

class accesorios(models.Model):#Borre fabricante
    tipo = models.CharField(max_length=30)
   
    def __str__(self):
        return f"{self.tipo,self.marca, self.modelo,self.precio}"

class perfiles(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono= models.IntegerField() 
    emial=models.EmailField(max_length=100)
    class Meta:
        abstract=True

class empleado(perfiles):
   cargo=models.CharField(max_length=30)
   def __str__(self):
    return f"{self.nombre,self.apellido, self.telefono,self.emial,self.cargo}"

class cliente(perfiles):
    edad=models.IntegerField()
    def __str__(self):
     return f"{self.nombre,self.apellido, self.telefono,self.emial,self.edad}"


class EnviarMensajes(models.Model):

    nombre=models.CharField(max_length=30)
    correo=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=30)
    mensaje=models.CharField(max_length=100)
       
    def __str__(self):
        return f"{self.nombre,self.correo,self.telefono, self.mensaje}"

#Comentar todo: selecciono . 1°ctrl+k . 2°ctrl+c (comentar) 2°ctrl+u (descomentar)