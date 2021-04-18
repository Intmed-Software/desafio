from django.contrib import admin
from .models import Disponibilidade, Horario

class HorarioAdminInline(admin.TabularInline):
    model = Horario

class DisponibilidadeAdmin(admin.ModelAdmin):
    inlines = (HorarioAdminInline, )

admin.site.register(Disponibilidade, DisponibilidadeAdmin)
