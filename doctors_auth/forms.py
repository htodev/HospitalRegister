"""Module which creates form on django model."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DoctorProfile


class RegisterForm(UserCreationForm):
    """It creates register form, on Django built-in User model."""

    class Meta:
        """This Meta class defines how RegisterForm will behave. """

        model = User
        fields = ['username']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileForm(forms.ModelForm):
    """It creates user ProfileForm form. """

    class Meta:
        """This Meta class defines how ProfileForm will behave. """

        model = DoctorProfile
        fields = ['profile_picture', 'name', 'specialty']


class LoginForm(forms.Form):
    """It creates log-in form. """

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

