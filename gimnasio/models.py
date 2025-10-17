from django.db import models

class Coach(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    especialidad = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dni = models.CharField("Documento", max_length=20, unique=True)
    fecha_nacimiento = models.DateField()

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.email})"


class Clase(models.Model):
    NIVEL_CHOICES = [
        ("B", "Beginner"),
        ("I", "Intermedio"),
        ("A", "Avanzado"),
    ]
    DIA_CHOICES = [
        ("lun", "Lunes"),
        ("mar", "Martes"),
        ("mie", "Miércoles"),
        ("jue", "Jueves"),
        ("vie", "Viernes"),
        ("sab", "Sábado"),
    ]

    dia = models.CharField(max_length=3, choices=DIA_CHOICES)
    hora = models.TimeField()
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES)
    cupos = models.PositiveSmallIntegerField(default=16)

    coach = models.ForeignKey(Coach, on_delete=models.PROTECT, related_name="clases")

    class Meta:
        ordering = ["dia", "hora"]

    def __str__(self):
        return f"{self.get_dia_display()} {self.hora} · {self.get_nivel_display()} · Coach {self.coach.apellido}"
