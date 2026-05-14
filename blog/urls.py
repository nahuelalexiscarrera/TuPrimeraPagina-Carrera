from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('pages/', views.ArticuloListView.as_view(), name='listado'),
    path('pages/<int:pk>/', views.ArticuloDetailView.as_view(), name='detalle'),
    path('pages/crear/', views.ArticuloCreateView.as_view(), name='crear_articulo'),
    path('pages/<int:pk>/editar/', views.ArticuloUpdateView.as_view(), name='editar_articulo'),
    path('pages/<int:pk>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),
]
