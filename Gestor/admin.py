from django.contrib import admin

# Register your models here.
from .models import Usuario
admin.site.register(Usuario)

from .models import Tarea
admin.site.register(Tarea)

from .models import Proyecto
admin.site.register(Proyecto)

from .models import Etiqueta
admin.site.register(Etiqueta)

from .models import AsignacionDeTarea
admin.site.register(AsignacionDeTarea)

from .models import Comentario
admin.site.register(Comentario)