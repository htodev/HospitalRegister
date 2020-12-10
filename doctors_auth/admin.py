"""Model which register DoctorProfile in Django Admin interface."""
from django.contrib import admin
from .models import DoctorProfile


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    """Configure DoctorProfile in Admin interface - exports list operation."""

    list_filter = ('specialty',)



