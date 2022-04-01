from django.db import models

# Create your models here.
class Persona(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=100)
    club = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    celular =models.CharField(max_length=11)
    pais = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    imagen = models.ImageField(null=True, blank = True)

class Meta:
    verbose_name = ('Persona')
    verbose_name_plural = ('Personas')

def __str__(self):
    return self.nombre