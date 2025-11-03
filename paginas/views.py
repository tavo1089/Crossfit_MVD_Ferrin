
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pagina

# Mixin para asegurar que solo el autor puede editar/borrar
class AutorRequiredMixin(UserPassesTestMixin):
	def test_func(self):
		obj = self.get_object()
		return obj.autor == self.request.user

class PaginaListView(ListView):
	model = Pagina
	template_name = "paginas/pages_list.html"
	context_object_name = "paginas"
	paginate_by = 6

	def get_queryset(self):
		queryset = super().get_queryset()
		q = self.request.GET.get("q")
		if q:
			queryset = queryset.filter(titulo__icontains=q) | queryset.filter(subtitulo__icontains=q)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["q"] = self.request.GET.get("q", "")
		return context

class PaginaDetailView(DetailView):
	model = Pagina
	template_name = "paginas/pages_detail.html"
	context_object_name = "pagina"

class PaginaCreateView(LoginRequiredMixin, CreateView):
	model = Pagina
	fields = ["titulo", "subtitulo", "contenido", "imagen"]
	template_name = "paginas/pages_form.html"
	success_url = reverse_lazy("pages_list")

	def form_valid(self, form):
		form.instance.autor = self.request.user
		return super().form_valid(form)

class PaginaUpdateView(LoginRequiredMixin, AutorRequiredMixin, UpdateView):
	model = Pagina
	fields = ["titulo", "subtitulo", "contenido", "imagen"]
	template_name = "paginas/pages_form.html"
	success_url = reverse_lazy("pages_list")

class PaginaDeleteView(LoginRequiredMixin, AutorRequiredMixin, DeleteView):
	model = Pagina
	template_name = "paginas/pages_confirm_delete.html"
	success_url = reverse_lazy("pages_list")
