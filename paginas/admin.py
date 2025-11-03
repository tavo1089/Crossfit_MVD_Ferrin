
# Register your models here.

from django.contrib import admin
from .models import Pagina

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
	list_display = ("titulo", "subtitulo", "autor", "fecha_publicacion")
	search_fields = ("titulo", "subtitulo", "contenido", "autor__username")
	list_filter = ("fecha_publicacion", "autor")
