from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import RegisterForm, ProfileForm, LoginForm


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
            'profile_form': ProfileForm()
        }
        return render(request, 'auth/register.html', context)
    else:
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print(dir(profile_form))
        if form.is_valid() and profile_form.is_valid():
            print(333333333)
            user = form.save()
            print(111111111)
            profile = profile_form.save(commit=False)
            print(222222222)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('landing-page')

        context = {
            'form': RegisterForm,
            'profile_form': ProfileForm(),
        }
        return render(request, 'landing-page', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }
        return render(request, 'auth/login.html', context)
    else:
        # user = authenticate(request, username='Hristo', password='qwerty1Q')
        # if user:
        login_form = LoginForm(request.POST)
        # return_url = get_redirect_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('enrollment-create')
        context = {
            'login_form': login_form,
        }
        return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing-page')