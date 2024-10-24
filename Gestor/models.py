from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.TextField(max_length=100)
    correo_electronico = models.TextField(unique=True)
    contraseña = models.TextField(max_length=100)
    fecha_de_registro = models.DateTimeField(default=timezone.now)
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completada', 'Completada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES) 
    completado = models.BooleanField(default=False) 
    fecha_de_creacion = models.DateField() 
    hora_de_vencimiento = models.TimeField()
    colaboradores = models.ManyToManyField(Usuario, related_name='proyectos_asignados')

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_de_inicio = models.DateField()
    fecha_de_finalizacion = models.DateField()  
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class AsignacionDeTarea(models.Model):
    observaciones = models.TextField()
    fecha_de_asignacion = models.DateTimeField(default=timezone.now) 
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_de_comentario = models.DateTimeField(default=timezone.now)