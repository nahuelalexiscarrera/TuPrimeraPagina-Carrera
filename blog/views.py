from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Articulo, Autor, Categoria
from .forms import ArticuloForm, BuscarArticuloForm


def inicio(request):
    ultimos = Articulo.objects.all()[:3]
    return render(request, 'index.html', {'ultimos': ultimos})


def about(request):
    return render(request, 'about.html')


class ArticuloListView(ListView):
    model = Articulo
    template_name = 'pages/listado.html'
    context_object_name = 'articulos'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = queryset.filter(titulo__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        q = self.request.GET.get('q', '')
        ctx['q'] = q
        ctx['form'] = BuscarArticuloForm(initial={'q': q})
        return ctx


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'pages/detalle.html'
    context_object_name = 'articulo'


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'pages/form_articulo.html'
    success_url = reverse_lazy('listado')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['accion'] = 'Crear'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Articulo publicado correctamente.')
        return super().form_valid(form)


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'pages/form_articulo.html'
    success_url = reverse_lazy('listado')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['accion'] = 'Editar'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Articulo actualizado correctamente.')
        return super().form_valid(form)


@login_required
def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        messages.success(request, 'Articulo eliminado.')
        return redirect('listado')
    return render(request, 'pages/confirmar_borrar.html', {'articulo': articulo})
