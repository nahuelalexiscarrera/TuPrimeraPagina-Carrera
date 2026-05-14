from django.urls import path
from . import views

urlpatterns = [
    path('', views.bandeja, name='bandeja'),
    path('nuevo/', views.nuevo_mensaje, name='nuevo_mensaje'),
    path('<int:usuario_id>/', views.conversacion, name='conversacion'),
]
