from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages

from .forms import RegistroForm, PerfilForm
from .models import Perfil


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(usuario=user)
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Hola de nuevo, {user.username}!')
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Sesion cerrada correctamente.')
    return redirect('inicio')


@login_required
def perfil(request):
    perfil_obj, _ = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil_obj})


@login_required
def editar_perfil(request):
    perfil_obj, _ = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil_obj)
    return render(request, 'accounts/editar_perfil.html', {'form': form})


@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contrasena actualizada correctamente.')
            return redirect('perfil')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/cambiar_password.html', {'form': form})
