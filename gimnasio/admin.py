from django.contrib import admin
from .models import Socio, Coach, Clase

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "email", "especialidad")
    search_fields = ("apellido", "nombre", "email", "especialidad")

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "email", "dni", "fecha_nacimiento")
    search_fields = ("apellido", "nombre", "email", "dni")
    list_filter = ("fecha_nacimiento",)

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ("dia", "hora", "nivel", "cupos", "coach")
    list_filter = ("dia", "nivel", "coach")
    search_fields = ("coach__apellido", "coach__nombre")
