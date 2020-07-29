from django.db import models
from django.contrib.auth.models import User
# from accounts.models import UserProfile

from .enums import SpecialityEnum


# Create your models here.
class Doctors(models.Model):

    """Defines Doctor model."""

    user = models.OneToOneField(User, models.DO_NOTHING)
    name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=20, choices=[(s.name, s.value) for s in SpecialityEnum])

    def __str__(self):
        return f"{self.name}"