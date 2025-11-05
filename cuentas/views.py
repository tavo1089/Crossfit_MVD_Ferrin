
# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Usuario o contraseña incorrectos.')
	return render(request, 'cuentas/login.html')

def logout_view(request):
	logout(request)
	return redirect('home')

def signup_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
	else:
		form = SignupForm()
	return render(request, 'cuentas/signup.html', {'form': form})
