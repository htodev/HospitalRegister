from django import forms


class PatientFilterForm(forms.Form):

    text = forms.CharField(
        required=False,
    )


class DoctorFilterForm(forms.Form):
    text = forms.CharField(
        required=False,
    )