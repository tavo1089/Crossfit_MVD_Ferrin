
from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
	nombre = models.CharField(max_length=100, blank=True)
	apellido = models.CharField(max_length=100, blank=True)
	bio = models.TextField(blank=True)
	avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
	fecha_nacimiento = models.DateField(blank=True, null=True)
	edad = models.PositiveIntegerField(blank=True, null=True)
	direccion = models.CharField(max_length=200, blank=True)
	pais = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return f"Perfil de {self.usuario.username}"
