from django.db import models
from medicos.models import Medico
from datetime import datetime
from rest_framework.exceptions import ValidationError

class Disponibilidade(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medicos', verbose_name='Doutor(a)')
    data = models.DateField(verbose_name='Data Disponível')

    def __str__(self):
        return self.data.strftime("%Y/%m/%d") + " [" + self.medico.nome + "]" 

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['data', 'medico'], name='Esse(a) Médico(a) já tem uma agenda para esse dia')
        ]
        verbose_name = "Agenda para médico"
        verbose_name_plural = "Agendas para médicos"

    def save(self, *args, **kwargs):
        if self.data < datetime.now().date():
            raise ValidationError({"detail": "Não pode registrar em uma data no passado."})
        super().save(*args, **kwargs)

class Horario(models.Model):
    disponibilidade = models.ForeignKey(Disponibilidade, on_delete=models.CASCADE, verbose_name='Disponibilidade')
    hora = models.TimeField(verbose_name='Horário Disponível')

    def __str__(self):
        return str(self.hora)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['disponibilidade', 'hora'], name='Horário já registrado na agenda')
        ]
        verbose_name = "Horário de Atendimento"
        verbose_name_plural = "Horários de Atendimento"
