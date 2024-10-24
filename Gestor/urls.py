from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('tareas/', views.listar_tareas, name='listar_tareas'),
    path('proyectos/', views.listar_proyectos, name='listar_proyectos'),
    path('etiquetas/', views.listar_etiquetas, name='listar_etiquetas'),
    path('asignaciones/', views.listar_asignaciones, name='listar_asignaciones'),
    path('comentarios/', views.listar_comentarios, name='listar_comentarios'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('proyectos/', views.listar_proyectos, name='listar_proyectos'),
    path('proyectos/<int:proyecto_id>/tareas/', views.listar_tareas_por_proyecto, name='listar_tareas_por_proyecto'),
    # Otras URLs que ya tengas definidas
]

