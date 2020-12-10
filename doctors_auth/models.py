"""It contains  DoctorProfile."""

from django.contrib.auth.models import User
from django.db import models


class DoctorProfile(models.Model):
    """Defines Doctor model."""

    KIND_CHOICES = (
        ('Urologist', 'Urologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Nephrologist', 'Nephrologist'),
        ('Endocrinologist', 'Endocrinologist'),
        ('Cardiologist', 'Cardiologist'),
        ('Virologist', 'Virologist'),
        ('Surgeon', 'Surgeon'),
    )

    profile_picture = models.ImageField(
        upload_to='users',
        blank=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=20, choices=KIND_CHOICES)

    def __str__(self):
        return f"{self.name}"
