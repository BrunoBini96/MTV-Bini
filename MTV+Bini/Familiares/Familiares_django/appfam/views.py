from email import charset
from unittest.util import _MAX_LENGTH
from django.forms import CharField
from django.shortcuts import render
from django.http import HttpResponse
from .models import familia
from .models import direcciones
from django.template import loader
# Create your views here.
def ingresar_familiares(request,nombre,apellido,telefono,nacimiento,pariente_de_mama):
    fam = familia(nombre=nombre, apellido=apellido, telefono=telefono,nacimiento=nacimiento,pariente_de_mama=pariente_de_mama)
    fam.save()
    #Tuve un error al momento de generar esta funcion, si hay muchos datos repetidos fue porque no me tomaba lo que sigue abajo del codigo pero si cargaba los datos en la DB
    plantilla = loader.get_template("agregar_fam.html")
    documento = plantilla.render({"my_nombre": nombre, "my_apellido" : apellido})
  
    return  HttpResponse (documento)  

def ingresar_direccion(request,calle,numeracion):
    direccion = direcciones(calle=calle, numeracion=numeracion)
    direccion.save()
    plantilla = loader.get_template("agregar_dir.html")
    documento = plantilla.render({"my_direccion" : calle, "my_numeracion" : numeracion})
    return HttpResponse(documento)
    
    
    