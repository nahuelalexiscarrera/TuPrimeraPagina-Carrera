from django.db import models
from django.contrib.auth.models import User


class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "mensajes"
        ordering = ['fecha']

    def __str__(self):
        return f"De {self.remitente} a {self.destinatario} — {self.fecha.strftime('%d/%m/%Y %H:%M')}"
