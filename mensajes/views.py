
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Mensaje
from .forms import MensajeForm
from django.db.models import Q

@login_required
def lista_conversaciones(request):
	usuarios = User.objects.exclude(id=request.user.id)
	conversaciones = []
	for usuario in usuarios:
		mensajes = Mensaje.objects.filter(
			(Q(remitente=request.user, destinatario=usuario) |
			 Q(remitente=usuario, destinatario=request.user))
		).order_by('fecha')
		if mensajes.exists():
			conversaciones.append({
				'usuario': usuario,
				'ultimo': mensajes.last(),
				'sin_leer': mensajes.filter(destinatario=request.user, leido=False).count()
			})
	return render(request, 'mensajes/conversaciones.html', {'conversaciones': conversaciones})

@login_required
def detalle_conversacion(request, usuario_id):
	otro = get_object_or_404(User, id=usuario_id)
	mensajes = Mensaje.objects.filter(
		(Q(remitente=request.user, destinatario=otro) |
		 Q(remitente=otro, destinatario=request.user))
	).order_by('fecha')
	mensajes.filter(destinatario=request.user, leido=False).update(leido=True)
	form = MensajeForm(initial={'destinatario': otro})
	return render(request, 'mensajes/detalle.html', {'mensajes': mensajes, 'otro': otro, 'form': form})

@login_required
def nuevo_mensaje(request):
	if request.method == 'POST':
		form = MensajeForm(request.POST)
		if form.is_valid():
			mensaje = form.save(commit=False)
			mensaje.remitente = request.user
			mensaje.save()
			messages.success(request, 'Mensaje enviado correctamente.')
			return redirect('mensajes_detalle', usuario_id=mensaje.destinatario.id)
	else:
		form = MensajeForm()
	return render(request, 'mensajes/nuevo.html', {'form': form})
