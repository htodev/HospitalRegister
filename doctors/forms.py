from django import forms
from .models import Doctors


class DoctorForms(forms.ModelForm):
    CHOICES = list(Doctors.KIND_CHOICES)

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    specialty = forms.ChoiceField(choices=CHOICES,
                                  widget=forms.Select(
                                      attrs={
                                          'class': 'form-control'
                                      }
                                  ))

    class Meta:
        model = Doctors
        fields = '__all__'