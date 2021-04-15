from django.db import models
from doctors.models import Medico
from datetime import datetime
from django.core.exceptions import ValidationError

class Dia(models.Model):
  data = models.DateField(verbose_name='Data Disponível')
  medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medicos', verbose_name='Doutor(a)')

  def __str__(self):
    return self.data.strftime("%Y/%m/%d") + " [" + self.medico.nome + "]" 

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['data', 'medico'], name='Esse(a) Médico(a) já tem uma agenda para esse dia')
    ]
    verbose_name = "Dia de Atendimento"
    verbose_name_plural = "Dias de Atendimento"

  def save(self, *args, **kwargs):
    if self.data <= datetime.now().date():
      raise ValidationError('Não pode registrar em uma data no passado.')
    super().save(*args, **kwargs)

  def horários(self):
    return Horario.objects.filter(data_id=self.id)

class Horario(models.Model):
  hora = models.TimeField(verbose_name='Horário Disponível')
  dia_id = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='dias', verbose_name='Dia')

  def __str__(self):
    return str(self.hora)

  class Meta:
    verbose_name = "Horário de Atendimento"
    verbose_name_plural = "Horários de Atendimento"
