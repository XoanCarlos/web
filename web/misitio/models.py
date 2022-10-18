from django.db import models
# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=150)
    fechalta = models.DateTimeField('Fecha Alta')
    direccion = models.CharField(max_length=150)
    movil = models.CharField(max_length=14)