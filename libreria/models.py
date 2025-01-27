from django.db import models

# Create your models here.
class Trabajador(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    rol = models.CharField(max_length=50) 



    def __str__(self):
        fila = self.nombre + ' -- ' + self.rut + ' -- ' + self.rol 
        return fila
   
    