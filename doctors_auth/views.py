"""This module contains functionality connected to 
register user, log-in user, log-out user, filling in doctor's profile data."""

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic

from .forms import RegisterForm, ProfileForm, LoginForm
from .models import DoctorProfile


def register_user(request):
    """This function register users."""
    
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
            'profile_form': ProfileForm()
        }
        return render(request, 'auth/register.html', context)
    else:
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('doctor profile')

        context = {
            'form': RegisterForm,
            'profile_form': ProfileForm(),
        }
        return render(request, 'doctor profile', context)


def login_user(request):
    """This function log-in users."""
    
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }
        return render(request, 'auth/login.html', context)
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('doctor profile')
        context = {
            'login_form': login_form,
        }
        return render(request, 'auth/login.html', context)


def logout_user(request):
    """This function log-out users."""
    
    logout(request)
    return redirect('landing-page')


def doctor_profile_landing_page(request):
    """This function filling in doctor data."""
    
    user = request.user
    context = {
        'user': user,
        'profile': user.doctorprofile,
        'form': ProfileForm()
    }
    return render(request, 'auth/profile/doctor_profile_landing_page.html', context)


class DoctorProfileUpdate(generic.UpdateView):
    """CBV for updating Doctor profile. """

    template_name = 'auth/profile/doctor_profile_edit.html'
    form_class = ProfileForm
    model = DoctorProfile
    success_url = '/auth/profile'

    def get_object(self, queryset=None):
        """It overrides built-in method in order to take PK of User dynamically
         and to return DoctorProfile. """

        pk = self.kwargs.get('pk', None)
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        return user.doctorprofile
