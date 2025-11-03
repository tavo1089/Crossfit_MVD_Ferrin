# ---------------------------------------------
# VISTA CLASES (tipos)
# Muestra las opciones de clases
# ---------------------------------------------
def clases(request):
    return render(request, "gimnasio/clases.html")
# ---------------------------------------------
# VISTA SUCURSALES
# Muestra las sucursales disponibles
# ---------------------------------------------
def sucursales(request):
    return render(request, "gimnasio/sucursales.html")

# IMPORTS 
from django.db.models import Q
from django.shortcuts import render
from .forms import BusquedaSocioForm, ClaseForm, CoachForm, SocioForm
from .models import Clase, Socio

# ---------------------------------------------
# VISTA ACERCA DE MÍ
# Muestra información personal del dueño del sitio
# ---------------------------------------------
def acerca_de_mi(request):
    return render(request, "gimnasio/acerca_de_mi.html")

# ---------------------------------------------
# HOME
# Página principal del sitio
# ---------------------------------------------
def home(request):
    return render(request, "gimnasio/index.html")

# ---------------------------------------------
# CRUD BÁSICO DE SOCIOS, COACHS Y CLASES
# Permite crear nuevos socios, coachs y clases
# ---------------------------------------------
def crear_socio(request):
    """Formulario para crear un nuevo socio"""
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gimnasio/form_success.html", {"titulo": "Socio creado"})
    else:
        form = SocioForm()
    return render(request, "gimnasio/form_generic.html", {"form": form, "titulo": "Nuevo socio"})

def crear_coach(request):
    """Formulario para crear un nuevo coach"""
    if request.method == "POST":
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gimnasio/form_success.html", {"titulo": "Coach creado"})
    else:
        form = CoachForm()
    return render(request, "gimnasio/form_generic.html", {"form": form, "titulo": "Nuevo coach"})

def crear_clase(request):
    """Formulario para crear una nueva clase"""
    if request.method == "POST":
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gimnasio/form_success.html", {"titulo": "Clase creada"})
    else:
        form = ClaseForm()
    return render(request, "gimnasio/form_generic.html", {"form": form, "titulo": "Nueva clase"})

# ---------------------------------------------
# BÚSQUEDA Y LISTADOS
# Listar y buscar socios y clases
# ---------------------------------------------
def buscar_socio(request):
    """Formulario y resultados para buscar socios por nombre, apellido o email"""
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
    """Listado de todos los socios"""
    socios = Socio.objects.order_by("apellido", "nombre")
    return render(request, "gimnasio/list_socios.html", {"socios": socios})

def listar_clases(request):
    """Listado de todas las clases, solo para usuarios autenticados"""
    if not request.user.is_authenticated:
        return render(request, "gimnasio/list_clases.html", {"clases": None})
    clases = Clase.objects.select_related("coach").order_by("dia", "hora")
    return render(request, "gimnasio/list_clases.html", {"clases": clases})
