from django.contrib import admin

# Register your models here.
from .models import Car



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price_per_day')