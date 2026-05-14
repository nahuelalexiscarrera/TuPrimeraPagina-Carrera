from django import forms
from django.contrib.auth.models import User
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('contenido',)
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje...'}),
        }
        labels = {
            'contenido': 'Mensaje',
        }


class NuevoMensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.none(),
        label='Para',
        empty_label='Selecciona un usuario',
    )

    class Meta:
        model = Mensaje
        fields = ('destinatario', 'contenido')
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje...'}),
        }
        labels = {
            'contenido': 'Mensaje',
        }

    def __init__(self, *args, current_user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if current_user:
            self.fields['destinatario'].queryset = User.objects.exclude(pk=current_user.pk)
