from django import forms
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            "nombre", "apellido", "bio", "avatar",
            "fecha_nacimiento", "edad", "direccion", "pais"
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "edad": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
        }
