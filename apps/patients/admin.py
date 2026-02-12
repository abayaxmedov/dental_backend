from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'blood_type', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'user__phone_number']
