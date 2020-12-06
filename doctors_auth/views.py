from django.contrib.auth import logout, authenticate, login
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
    logout(request)
    return redirect('landing-page')


def doctor_profile_landing_page(request):
    user = request.user
    context = {
        'user': user,
        'profile': user.doctorprofile,
        'form': ProfileForm()
    }
    return render(request, 'auth/profile/doctor_profile_landing_page.html', context)


def doctor_profile_edit(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'user': user,
            'profile': user.doctorprofile,
            'form': ProfileForm()
        }
        return render(request, 'auth/profile/doctor_profile_edit.html', context)
    else:
        print(dir(request))
        print(request.method)
        form = ProfileForm(request.POST, request.FILES, instance=user.doctorprofile)
        if form.is_valid():
            form.save()
            return redirect('doctor profile')
        return redirect('doctor profile')
