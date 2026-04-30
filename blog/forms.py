from django import forms


class AutorForm(forms.Form):
    """Formulario para crear un nuevo Autor."""
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()


class CategoriaForm(forms.Form):
    """Formulario para crear una nueva Categoria."""
    nombre = forms.CharField(max_length=50)


class ArticuloForm(forms.Form):
    """Formulario para crear un nuevo Articulo."""
    titulo = forms.CharField(max_length=200)
    contenido = forms.CharField(widget=forms.Textarea)
    autor = forms.IntegerField(widget=forms.Select)
    categoria = forms.IntegerField(widget=forms.Select)


class BuscarArticuloForm(forms.Form):
    """Formulario para buscar articulos en la base de datos."""
    titulo = forms.CharField(max_length=200, required=False)
