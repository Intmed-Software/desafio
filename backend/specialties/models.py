from django.db import models
from datetime import datetime

class Specialty(models.Model):
  name = models.CharField(max_length=64, unique=True, verbose_name='Nome')
  created_at = models.DateTimeField(verbose_name='Criada em')
  updated_at = models.DateTimeField(verbose_name='Atualizada em')
  removed_at = models.DateTimeField(blank=True, null=True, verbose_name='Removida em')

  def __str__(self):
        return self.name

  class Meta:
    verbose_name = "Especialidade"
    verbose_name_plural = "Especialidades"

  def save(self, *args, **kwargs):
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(today)
    if self.id:
      self.updated_at = today
    else:
      self.created_at = today
      self.updated_at = today
    super().save(*args, **kwargs)
