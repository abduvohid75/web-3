
from django.contrib import admin

from main.models import student


# Register your models here.
@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description',)
