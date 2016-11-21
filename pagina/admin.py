from django.contrib import admin
from .models import Prioridad, Dificultad, Actividad, Proyecto, Empresa, Asignacion

admin.site.register(Prioridad)
admin.site.register(Dificultad)
admin.site.register(Actividad)
admin.site.register(Proyecto)
admin.site.register(Empresa)
admin.site.register(Asignacion)

# Register your models here.
