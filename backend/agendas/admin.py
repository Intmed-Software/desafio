from django.contrib import admin
from .models import Dia, Horario

class HorarioAdminInline(admin.TabularInline):
    model = Horario

class DiaAdmin(admin.ModelAdmin):
    inlines = (HorarioAdminInline, )

admin.site.register(Dia, DiaAdmin)
