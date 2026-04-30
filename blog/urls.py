from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear-articulo/', views.crear_articulo, name='crear_articulo'),
    path('buscar/', views.buscar_articulos, name='buscar_articulos'),
]
