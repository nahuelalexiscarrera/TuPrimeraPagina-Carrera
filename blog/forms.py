from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Articulo, Autor, Categoria


class ArticuloForm(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Articulo
        fields = ('titulo', 'subtitulo', 'contenido', 'imagen', 'autor', 'categoria')


class BuscarArticuloForm(forms.Form):
    q = forms.CharField(
        max_length=200,
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar articulos...'})
    )
