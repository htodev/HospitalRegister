"""Module which creates form for search bar."""

from django import forms


class PatientFilterForm(forms.Form):
    """Defines search bar for patients. """

    text = forms.CharField(
        required=False,
    )


class DoctorFilterForm(forms.Form):
    """Defines search bar for doctors. """

    text = forms.CharField(
        required=False,
    )