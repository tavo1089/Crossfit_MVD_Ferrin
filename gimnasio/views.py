# gimnasio/views.py
# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
from django.db.models import Q
from django.shortcuts import render

from .forms import BusquedaSocioForm, ClaseForm, CoachForm, SocioForm
from .models import Clase, Socio


# -------------------------------------------------
# HOME
# -------------------------------------------------
def home(request):
    return render(request, "gimnasio/index.html")


# -------------------------------------------------
# CRUD BÁSICO
# -------------------------------------------------
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


# -------------------------------------------------
# BÚSQUEDA Y LISTADOS
# -------------------------------------------------
def buscar_socio(request):
    form = BusquedaSocioForm(request.GET or None)
    resultados = []

    if form.is_valid() and form.cleaned_data.get("q"):
        q = form.cleaned_data["q"]
        resultados = (
            Socio.objects.filter(
                Q(nombre__icontains=q) |
                Q(apellido__icontains=q) |
                Q(email__icontains=q)
            )
            .order_by("apellido", "nombre")
        )

    return render(
        request,
        "gimnasio/buscar_socio.html",
        {"form": form, "resultados": resultados},
    )


def listar_socios(request):
    socios = Socio.objects.order_by("apellido", "nombre")
    return render(request, "gimnasio/list_socios.html", {"socios": socios})


def listar_clases(request):
    clases = Clase.objects.select_related("coach").order_by("dia", "hora")
    return render(request, "gimnasio/list_clases.html", {"clases": clases})
