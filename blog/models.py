from django.db import models


class Autor(models.Model):
    """Modelo que representa a un autor de articulos del blog."""
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "autores"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    """Modelo que representa una categoria para clasificar articulos."""
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    """Modelo que representa un articulo/post del blog."""
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
