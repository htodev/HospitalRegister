from django.shortcuts import render


def landing_page(request):
    return render(request, 'landing_page.html')


def doctor_profile_landing_page(request):
    return render(request, 'auth/profile/doctor_profile_landing_page.html')

