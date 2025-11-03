from django.urls import path
from . import views

urlpatterns = [
    path('mi-perfil/', views.mi_perfil, name='mi_perfil'),
    path('editar/', views.editar_perfil, name='editar_perfil'),
    path('cambiar-password/', views.cambiar_password, name='cambiar_password'),
]
