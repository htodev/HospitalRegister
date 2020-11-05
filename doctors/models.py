from django.db import models
from django.contrib.auth.models import User
# from accounts.models import UserProfile

# from .enums import SpecialityEnum


# Create your models here.
class Doctors(models.Model):

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=20, choices=KIND_CHOICES)

    def __str__(self):
        return f"{self.name}"