
from django.contrib import admin

from main.models import Product, Category


# Register your models here.
@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)