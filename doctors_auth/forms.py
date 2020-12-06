from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DoctorProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['profile_picture', 'name', 'specialty']
        # exclude = ['user']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

