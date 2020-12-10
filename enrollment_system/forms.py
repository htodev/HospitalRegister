"""Module which creates form on django model."""

from datetime import datetime
from django import forms
from django.forms import SelectDateWidget
from .models import Enrollment


class EnrollmentForm(forms.ModelForm):
    """It creates enrollment form, on Enrollment model."""

    patient_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    symptoms = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    diagnosis = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    received_at = forms.DateTimeField(initial=datetime.now(), widget=SelectDateWidget(
        attrs={
            'class': 'form-control'
        }
    ))

    room_number = forms.IntegerField(required=True,
                                     min_value=0,
                                     widget=forms.NumberInput(
                                         attrs={
                                             'class': 'form-control'
                                         }
                                     ))

    class Meta:
        """This Meta class defines how EnrollmentForm will behave. """

        model = Enrollment
        fields = '__all__'
