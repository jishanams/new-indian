from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_model', 'service_type', 'preferred_date', 'created_at')
    list_filter = ('service_type', 'preferred_date', 'created_at')
    search_fields = ('name', 'phone', 'vehicle_model', 'registration_no')
