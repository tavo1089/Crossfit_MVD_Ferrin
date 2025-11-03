
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Perfil
from .forms import PerfilForm

@login_required
def mi_perfil(request):
	perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
	return render(request, "perfiles/mi_perfil.html", {"perfil": perfil})

@login_required
def editar_perfil(request):
	perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
	if request.method == "POST":
		form = PerfilForm(request.POST, request.FILES, instance=perfil)
		if form.is_valid():
			form.save()
			messages.success(request, "Perfil actualizado correctamente.")
			return redirect("mi_perfil")
	else:
		form = PerfilForm(instance=perfil)
	return render(request, "perfiles/editar_perfil.html", {"form": form})

# Cambiar contraseña del usuario logueado
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def cambiar_password(request):
	if request.method == "POST":
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, "Contraseña cambiada correctamente.")
			return redirect("mi_perfil")
	else:
		form = PasswordChangeForm(request.user)
	return render(request, "perfiles/cambiar_password.html", {"form": form})
