from django.shortcuts import render,get_object_or_404
from .models import Usuario, Tarea, Proyecto, Etiqueta, AsignacionDeTarea, Comentario

def home(request):
    return render(request, 'home.html')

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def listar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'listar_tareas.html', {'tareas': tareas})

def listar_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'listar_etiquetas.html', {'etiquetas': etiquetas})

def listar_asignaciones(request):
    asignaciones = AsignacionDeTarea.objects.all()
    return render(request, 'listar_asignaciones.html', {'asignaciones': asignaciones})

def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'listar_comentarios.html', {'comentarios': comentarios})

def listar_tareas_por_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    tareas = Tarea.objects.filter(colaboradores=proyecto.creador).order_by('-fecha_de_creacion')
    return render(request, 'listar_tareas_por_proyecto.html', {'proyecto': proyecto, 'tareas': tareas})
