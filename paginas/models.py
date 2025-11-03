
# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

class Pagina(models.Model):
	titulo = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=150)
	contenido = RichTextField()
	imagen = models.ImageField(upload_to="pages_images/", blank=True, null=True)
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="paginas")

	class Meta:
		ordering = ["-fecha_publicacion"]

	def __str__(self):
		return self.titulo
