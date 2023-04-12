from django.db import models

# Create your models here.
class Alum(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    edad = models.IntegerField()
    poblacion = models.DateField()
    graduado = models.BooleanField()
class Prof(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    edad = models.IntegerField()
    poblacion = models.DateField()
    graduado = models.BooleanField()
