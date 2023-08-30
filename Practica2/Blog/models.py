from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo