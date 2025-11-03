from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaginaListView.as_view(), name='pages_list'),
    path('<int:pk>/', views.PaginaDetailView.as_view(), name='pages_detail'),
    path('crear/', views.PaginaCreateView.as_view(), name='pages_create'),
    path('<int:pk>/editar/', views.PaginaUpdateView.as_view(), name='pages_update'),
    path('<int:pk>/borrar/', views.PaginaDeleteView.as_view(), name='pages_delete'),
]
