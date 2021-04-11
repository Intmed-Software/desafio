from django.db import models
from doctors.models import Doctor
from datetime import datetime

class Day(models.Model):
    date = models.DateField(verbose_name='Dia Disponível')
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, verbose_name='Doutor(a)', unique=False)

    def __str__(self):
        return self.date.strftime("%Y/%m/%d") + " [" + self.doctor.name + "]" 

    class Meta:
        # constraints = [
        #     models.UniqueConstraint(fields=['date', 'doctor'], name='Unique Doctor Date')
        # ]
        verbose_name = "Data"
        verbose_name_plural = "Datas"

class Hour(models.Model):
    hour = models.TimeField(verbose_name='Horário Disponível')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='days', verbose_name='Dia')

    # def __str__(self):
    #     return datetime.strptime(self.hour, "%H:%M:%S")

    
    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Horários"
