from django.db import models
from datetime import datetime
from specialties.models import Specialty

class Doctor(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Nome')
    crm = models.CharField(max_length=64, unique=True, verbose_name='CRM')
    email = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name='E-mail')
    phone = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name='Telefone')
    created_at = models.DateTimeField(verbose_name='Cadastrado(a) em')
    updated_at = models.DateTimeField(verbose_name='Atualizado(a) em')
    removed_at = models.DateTimeField(blank=True, null=True, verbose_name='Desligado(a) em')
    specialties = models.ManyToManyField(Specialty, verbose_name='Especialidades')

    def __str__(self):
        return "[ " + self.crm + " ]" + " - " + self.name

    class Meta:
        verbose_name = "Médico(a)"
        verbose_name_plural = "Médicos(as)"

    def save(self, *args, **kwargs):
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(today)
        if self.id:
            self.updated_at = today
        else:
            self.created_at = today
            self.updated_at = today
        super().save(*args, **kwargs)
