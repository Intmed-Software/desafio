from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
  exclude = ('created_at','updated_at','removed_at',)

admin.site.register(Doctor, DoctorAdmin)
