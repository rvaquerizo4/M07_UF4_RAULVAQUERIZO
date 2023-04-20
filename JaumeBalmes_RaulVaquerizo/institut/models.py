from django.db import models

# Create your models here.
class Alum(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=50)
    clase = models.CharField(max_length=50)
class Prof(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=50)
    clase = models.CharField(max_length=50)
