
# creando la vista para la pagina principal
from django.shortcuts import render

def home(request):
    return render(request, 'gimnasio/index.html')

from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import SocioForm, CoachForm, ClaseForm, BusquedaSocioForm
from .models import Socio

def crear_socio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gimnasio/form_success.html", {"titulo": "Socio creado"})
    else:
        form = SocioForm()
    return render(request, "gimnasio/form_generic.html", {"form": form, "titulo": "Nuevo socio"})

def crear_coach(request):
    if request.method == "POST":
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gimnasio/form_success.html", {"titulo": "Coach creado"})
    else:
        form = CoachForm()
    return render(request, "gimnasio/form_generic.html", {"form": form, "titulo": "Nuevo coach"})

def crear_clase(request):
    if request.method == "POST":
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gimnasio/form_success.html", {"titulo": "Clase creada"})
    else:
        form = ClaseForm()
    return render(request, "gimnasio/form_generic.html", {"form": form, "titulo": "Nueva clase"})

def buscar_socio(request):
    form = BusquedaSocioForm(request.GET or None)
    resultados = []
    if form.is_valid() and form.cleaned_data.get("q"):
        q = form.cleaned_data["q"]
        resultados = Socio.objects.filter(
            Q(apellido__icontains=q) | Q(email__icontains=q)
        ).order_by("apellido", "nombre")
    return render(request, "gimnasio/buscar_socio.html", {"form": form, "resultados": resultados})

# creando la vista para listar socios y clases
from .models import Socio, Clase

def listar_socios(request):
    socios = Socio.objects.order_by("apellido", "nombre")
    return render(request, "gimnasio/list_socios.html", {"socios": socios})

def listar_clases(request):
    clases = Clase.objects.select_related("coach").order_by("dia", "hora")
    return render(request, "gimnasio/list_clases.html", {"clases": clases})
