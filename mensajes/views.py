from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

from .models import Mensaje
from .forms import MensajeForm, NuevoMensajeForm


@login_required
def bandeja(request):
    contactos_ids = Mensaje.objects.filter(
        Q(remitente=request.user) | Q(destinatario=request.user)
    ).values_list('remitente', 'destinatario')

    ids_set = set()
    for r, d in contactos_ids:
        ids_set.add(r)
        ids_set.add(d)
    ids_set.discard(request.user.pk)

    contactos = User.objects.filter(pk__in=ids_set)
    no_leidos = Mensaje.objects.filter(destinatario=request.user, leido=False).count()

    return render(request, 'mensajes/bandeja.html', {
        'contactos': contactos,
        'no_leidos': no_leidos,
    })


@login_required
def conversacion(request, usuario_id):
    otro = get_object_or_404(User, pk=usuario_id)
    mensajes_conv = Mensaje.objects.filter(
        Q(remitente=request.user, destinatario=otro) |
        Q(remitente=otro, destinatario=request.user)
    )
    mensajes_conv.filter(destinatario=request.user, leido=False).update(leido=True)

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.remitente = request.user
            msg.destinatario = otro
            msg.save()
            return redirect('conversacion', usuario_id=otro.pk)
    else:
        form = MensajeForm()

    return render(request, 'mensajes/conversacion.html', {
        'otro': otro,
        'mensajes': mensajes_conv,
        'form': form,
    })


@login_required
def nuevo_mensaje(request):
    if request.method == 'POST':
        form = NuevoMensajeForm(request.POST, current_user=request.user)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.remitente = request.user
            msg.save()
            messages.success(request, 'Mensaje enviado.')
            return redirect('conversacion', usuario_id=msg.destinatario.pk)
    else:
        form = NuevoMensajeForm(current_user=request.user)
    return render(request, 'mensajes/nuevo_mensaje.html', {'form': form})
