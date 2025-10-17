
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('socios/nuevo/', views.crear_socio, name='crear_socio'),
    path('coachs/nuevo/', views.crear_coach, name='crear_coach'),
    path('clases/nueva/', views.crear_clase, name='crear_clase'),
    path('socios/buscar/', views.buscar_socio, name='buscar_socio'),
    path('socios/', views.listar_socios, name='listar_socios'),
    path('clases/', views.listar_clases, name='listar_clases'),

]
