from django.contrib import admin
from .models import Specialty

class SpecialtyAdmin(admin.ModelAdmin):
  exclude = ('created_at','updated_at','removed_at',)

admin.site.register(Specialty, SpecialtyAdmin)
