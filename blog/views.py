from django.shortcuts import render, redirect
from django import forms

from .models import Autor, Categoria, Articulo
from .forms import AutorForm, CategoriaForm, ArticuloForm, BuscarArticuloForm


def inicio(request):
    """Vista principal - index."""
    return render(request, 'index.html')


# --- Vistas de carga ---

def crear_autor(request):
    """Formulario para registrar un nuevo autor."""
    if request.method == 'POST':
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            Autor.objects.create(
                nombre=datos['nombre'],
                apellido=datos['apellido'],
                email=datos['email'],
            )
            return render(request, 'pages/crear_autor.html', {
                'formulario': AutorForm(),
                'mensaje': 'Autor registrado correctamente.',
            })
    else:
        formulario = AutorForm()

    return render(request, 'pages/crear_autor.html', {'formulario': formulario})


def crear_categoria(request):
    """Formulario para registrar una nueva categoria."""
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            Categoria.objects.create(nombre=datos['nombre'])
            return render(request, 'pages/crear_categoria.html', {
                'formulario': CategoriaForm(),
                'mensaje': 'Categoria registrada correctamente.',
            })
    else:
        formulario = CategoriaForm()

    return render(request, 'pages/crear_categoria.html', {'formulario': formulario})


def crear_articulo(request):
    """Formulario para redactar un nuevo articulo."""
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        formulario = ArticuloForm(request.POST)
        formulario.fields['autor'].widget = forms.Select(
            choices=[(a.id, str(a)) for a in autores]
        )
        formulario.fields['categoria'].widget = forms.Select(
            choices=[(c.id, str(c)) for c in categorias]
        )
        if formulario.is_valid():
            datos = formulario.cleaned_data
            autor = Autor.objects.get(id=datos['autor'])
            categoria = Categoria.objects.get(id=datos['categoria'])
            Articulo.objects.create(
                titulo=datos['titulo'],
                contenido=datos['contenido'],
                autor=autor,
                categoria=categoria,
            )
            formulario_nuevo = ArticuloForm()
            formulario_nuevo.fields['autor'].widget = forms.Select(
                choices=[(a.id, str(a)) for a in autores]
            )
            formulario_nuevo.fields['categoria'].widget = forms.Select(
                choices=[(c.id, str(c)) for c in categorias]
            )
            return render(request, 'pages/crear_articulo.html', {
                'formulario': formulario_nuevo,
                'mensaje': 'Articulo publicado correctamente.',
            })
    else:
        formulario = ArticuloForm()
        formulario.fields['autor'].widget = forms.Select(
            choices=[(a.id, str(a)) for a in autores]
        )
        formulario.fields['categoria'].widget = forms.Select(
            choices=[(c.id, str(c)) for c in categorias]
        )

    return render(request, 'pages/crear_articulo.html', {'formulario': formulario})


# --- Vista de busqueda ---

def buscar_articulos(request):
    """Buscar articulos por titulo en la base de datos."""
    formulario = BuscarArticuloForm()
    resultados = []

    if request.method == 'GET' and 'titulo' in request.GET:
        formulario = BuscarArticuloForm(request.GET)
        if formulario.is_valid():
            titulo = formulario.cleaned_data['titulo']
            if titulo:
                resultados = Articulo.objects.filter(titulo__icontains=titulo)

    return render(request, 'pages/buscar_articulos.html', {
        'formulario': formulario,
        'resultados': resultados,
    })
