from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Elige tu nombre de usuario',
            'title': 'Nombre de usuario: solo letras, números y guiones bajos.'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'tu@email.com',
            'title': 'Correo electrónico válido.'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Crea una contraseña segura (min. 8 caracteres)',
            'title': 'Contraseña segura: mínimo 8 caracteres, letras y números.'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Repite la contraseña anterior',
            'title': 'Repite la contraseña exactamente igual.'
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
