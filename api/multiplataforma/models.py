from django.db import models

# Create your models here.
class Recetas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    imagen  = models.ImageField(upload_to='dataInformation', null=True, blank=True)
    tipo = models.CharField(max_length=100, default='tipo de comida')
    pasos = models.CharField(max_length=500, default='Aqui iran los pasos de la receta')
    favoritos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre