from django.conf import settings
from django.db import models
from datetime import datetime
from rest_framework.exceptions import ValidationError
from agendas.models import Disponibilidade, Horario

class Consulta(models.Model):
    disponibilidade = models.ForeignKey(Disponibilidade, on_delete=models.CASCADE, verbose_name='Disponibilidade')
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name='Horário')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')
    data_agendamento = models.DateTimeField(verbose_name='Data do Agendamento')

    def __str__(self):
        return str(self.disponibilidade) + " - " + str(self.horario)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['disponibilidade', 'horario'], name='Horário já reservado.')
        ]
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def save(self, *args, **kwargs):
        disponibilidade = Disponibilidade.objects.get(id=self.disponibilidade.id)
        if disponibilidade.data < datetime.now().date():
            raise ValidationError({"detail": "Não é possível marcar uma consulta em uma data no passado."})
        horario = Horario.objects.get(id=self.horario.id)
        if disponibilidade.data == datetime.now().date() and horario.hora < datetime.now().time():
            raise ValidationError({"detail": "Não é possível marcar uma consulta em um horário no passado."})
        self.data_agendamento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().save(*args, **kwargs)

    def delete(self):
        disponibilidade = Disponibilidade.objects.get(id=self.disponibilidade.id)
        if disponibilidade.data < datetime.now().date():
            raise ValidationError({"detail": "Não é possível desmarcar uma consulta em uma data no passado."})
        horario = Horario.objects.get(id=self.horario.id)
        if disponibilidade.data == datetime.now().date() and horario.hora < datetime.now().time():
            raise ValidationError({"detail": "Não é possível desmarcar uma consulta em um horário no passado."})
        super().delete()

