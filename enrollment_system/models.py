"""Contains Enrollment model"""

from django.db import models
from doctors_auth.models import DoctorProfile


class Enrollment(models.Model):
    """Defines Enrollment model"""

    doctor_name = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    symptoms = models.CharField(max_length=80)
    diagnosis = models.CharField(max_length=30)
    received_at = models.DateTimeField(auto_now=True)
    room_number = models.PositiveIntegerField()
