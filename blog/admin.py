from django.contrib import admin

from .models import Autor, Categoria, Articulo

admin.site.register([Autor, Categoria, Articulo])
