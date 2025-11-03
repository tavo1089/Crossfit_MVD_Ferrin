from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ["destinatario", "texto"]
        widgets = {
            "destinatario": forms.Select(attrs={"class": "form-select"}),
            "texto": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Escribe tu mensaje..."}),
        }
