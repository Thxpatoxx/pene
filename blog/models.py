from django.db import models

class Implementodep(models.Model):
    ESTADO = (
        ('NO DISPONIBLE','NO DISPONIBLE'),
        ('DISPONIBLE','DISPONIBLE'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')
    IMPLEMENTO = (
        ('PALETAS','PALETAS'),
        ('PELOTA PINPONG','PELOTA PINPONG'),
        ('PELOTA FOOTBALL','PELOTA FOOTBALL'),
        ('PELOTA BASCKETBALL','PELOTA BASCKETBALL'),
        ('CANCHA','CANCHA'),
    )
    implemento = models.CharField(max_length=80,choices=IMPLEMENTO,default='PALETAS')
    observación = models.TextField(max_length=200,default='Implemento sin detalle')