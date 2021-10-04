from django.contrib import admin
from .models import Project


class CoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
# Register your models here.
admin.site.register(Project, CoreAdmin)