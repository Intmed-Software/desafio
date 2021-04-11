from django.contrib import admin
from .models import Day, Hour

class HourAdminInline(admin.TabularInline):
    model = Hour

class DayAdmin(admin.ModelAdmin):
    inlines = (HourAdminInline, )

admin.site.register(Day, DayAdmin)
