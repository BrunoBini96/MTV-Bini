from email import charset
from django.db import models
from unittest.util import _MAX_LENGTH
# Create your models here.
class familia(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    #el booleano TRUE o 1 es que es pariente de la madre, el 0 o false es que es pariente del padre.
    pariente_de_mama = models.BooleanField()

class direcciones(models.Model):
    calle = models.CharField( max_length=50)
    numeracion = models.IntegerField()

