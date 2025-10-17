from django import forms
from .models import Socio, Coach, Clase

class DateInput(forms.DateInput):
    input_type = "date"

class TimeInput(forms.TimeInput):
    input_type = "time"

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ["nombre", "apellido", "email", "dni", "fecha_nacimiento"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_nacimiento": DateInput(attrs={"class": "form-control"}),
        }

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ["nombre", "apellido", "email", "especialidad"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "especialidad": forms.TextInput(attrs={"class": "form-control"}),
        }

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ["dia", "hora", "nivel", "cupos", "coach"]
        widgets = {
            "dia": forms.Select(attrs={"class": "form-select"}),
            "hora": TimeInput(attrs={"class": "form-control"}),
            "nivel": forms.Select(attrs={"class": "form-select"}),
            "cupos": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "coach": forms.Select(attrs={"class": "form-select"}),
        }

class BusquedaSocioForm(forms.Form):
    q = forms.CharField(
        label="Apellido o email",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ej: Gómez o pedro@mvd.com"
        })
    )
