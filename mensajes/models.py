
from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
	remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
	destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
	texto = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)
	leido = models.BooleanField(default=False)

	class Meta:
		ordering = ["fecha"]

	def __str__(self):
		return f"De {self.remitente} para {self.destinatario} ({self.fecha:%d/%m/%Y %H:%M})"
