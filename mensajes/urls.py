from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_conversaciones, name='mensajes_conversaciones'),
    path('conversacion/<int:usuario_id>/', views.detalle_conversacion, name='mensajes_detalle'),
    path('nuevo/', views.nuevo_mensaje, name='mensajes_nuevo'),
]
