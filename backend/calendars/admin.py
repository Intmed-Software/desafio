from django.contrib import admin
from .models import Workday, Workhour

class WorkhourAdminInline(admin.TabularInline):
    model = Workhour

class WorkdayAdmin(admin.ModelAdmin):
    inlines = (WorkhourAdminInline, )

admin.site.register(Workday, WorkdayAdmin)
