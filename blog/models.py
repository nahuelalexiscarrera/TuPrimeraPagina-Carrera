from django.db import models
from ckeditor.fields import RichTextField


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "autores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "articulos"
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo
