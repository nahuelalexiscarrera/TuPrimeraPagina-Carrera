from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class PerfilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False, label='Nombre')
    last_name = forms.CharField(max_length=50, required=False, label='Apellido')

    class Meta:
        model = Perfil
        fields = ('avatar', 'biografia', 'fecha_nacimiento')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.usuario_id:
            self.fields['first_name'].initial = self.instance.usuario.first_name
            self.fields['last_name'].initial = self.instance.usuario.last_name

    def save(self, commit=True):
        perfil = super().save(commit=False)
        perfil.usuario.first_name = self.cleaned_data['first_name']
        perfil.usuario.last_name = self.cleaned_data['last_name']
        perfil.usuario.save()
        if commit:
            perfil.save()
        return perfil
