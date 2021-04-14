from django.db import models
from doctors.models import Doctor
from datetime import datetime
from django.core.exceptions import ValidationError

class Workday(models.Model):
    date = models.DateField(verbose_name='Dia Disponível')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctors', verbose_name='Doutor(a)')

    def __str__(self):
        return self.date.strftime("%Y/%m/%d") + " [" + self.doctor.name + "]" 

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'doctor'], name='Esse(a) Médico(a) já tem uma agenda para esse dia')
        ]
        verbose_name = "Dia de Atendimento"
        verbose_name_plural = "Dias de Atendimento"

    def save(self, *args, **kwargs):
        if self.date <= datetime.now().date():
            raise ValidationError('Não pode registrar em uma data no passado.')
        super().save(*args, **kwargs)

    def hours(self):
        return Workhour.objects.filter(day=self.id)

class Workhour(models.Model):
    hour = models.TimeField(verbose_name='Horário Disponível')
    day = models.ForeignKey(Workday, on_delete=models.CASCADE, related_name='days', verbose_name='Dia')

    def __str__(self):
        return str(self.hour)

    class Meta:
        verbose_name = "Horário de Atendimento"
        verbose_name_plural = "Horários de Atendimento"
