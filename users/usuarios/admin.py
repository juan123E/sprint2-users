from django.contrib import admin
from .models import Usuario, Gestor, ResponsableFinanciero, Estudiante, ResponsableEstudiante
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Gestor)
admin.site.register(ResponsableFinanciero)
admin.site.register(Estudiante)
admin.site.register(ResponsableEstudiante)
