from django.db import models
from especialidades.models import Especialidade

class Medico(models.Model):
    nome = models.CharField(max_length=64, unique=True, verbose_name='Nome')
    crm = models.CharField(max_length=64, unique=True, verbose_name='CRM')
    email = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name='E-mail')
    telefone = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name='Telefone')
    especialidade = models.ForeignKey(Especialidade, on_delete=models.RESTRICT, verbose_name='Especialidade')

    def __str__(self):
        return "[ " + self.crm + " ]" + " - " + self.nome

    class Meta:
        verbose_name = "Médico(a)"
        verbose_name_plural = "Médicos(as)"