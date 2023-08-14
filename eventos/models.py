from django.db import models
from django.utils import timezone

# Create your models here.
class Evento(models.Model):    
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)    
    inicio = models.DateField()
    fin = models.DateField()
    diploma = models.BooleanField(default=0)
    foto = models.ImageField(upload_to='images/', null=True, blank=True)
    descripcion = models.TextField()
    activo = models.BooleanField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    #created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.nombre

class Pais(models.Model):    
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'paises'

    def __str__(self):
        return self.nombre

tipo_contacto =[
    (1, 'No puedo Entrar'),
    (2, 'No aparece mi Evento'),
    (3, 'Otros')
]
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo = models.IntegerField(choices=tipo_contacto)
    mensaje = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    

