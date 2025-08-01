from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Car, Reservation

class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0
    readonly_fields = ('car', 'start_date', 'end_date', 'created_at')

class CustomUserAdmin(BaseUserAdmin):
    inlines = [ReservationInline]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price_per_day')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'created_at')
    list_filter = ('car', 'start_date')
    search_fields = ('user__username', 'car__brand', 'car__model')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)