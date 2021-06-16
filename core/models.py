from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

#MODELO ARTISTA
class Artista(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(2)],max_length=50,verbose_name="Nombre Artista")
    descripcion = models.CharField(validators=[MinLengthValidator(10)],max_length=200,verbose_name="Descripcion",null=True,blank=True)
    img_artista = models.ImageField(upload_to="static/core/img",verbose_name="Imagen Artista")

    def __str__(self):
        return self.nombre

#MODELO PINTURA LA CUAL SE RELACIONA CON ARTISTA
class Pintura(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    nombre = models.CharField(validators=[MinLengthValidator(2)],max_length=50,verbose_name="Nombre Pintura")
    historia = models.CharField(validators=[MinLengthValidator(10)],max_length=200,verbose_name="Historia",null=True,blank=True)
    descripcion = models.CharField(validators=[MinLengthValidator(10)],max_length=200,verbose_name="Descripcion",null=True,blank=True)
    img_pintura = models.ImageField(upload_to="static/core/img",verbose_name="Imagen Pintura")
    precio = models.FloatField(default=0.0,verbose_name="Precio")
    tecnica = models.CharField(validators=[MinLengthValidator(2)],max_length=50,verbose_name="Tecnica",blank=True,null=True)

    def __str__(self):
        return self.nombre
