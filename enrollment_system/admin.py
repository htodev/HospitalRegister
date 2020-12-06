from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    list_display = ('doctor_name', 'patient_name', 'received_at')
    search_fields = ['doctor_name__name', 'patient_name']
    list_filter = ('received_at', 'room_number')


