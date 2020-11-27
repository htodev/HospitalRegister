from django.shortcuts import render

from enrollment_system.models import Enrollment
from doctors_auth.models import DoctorProfile


def all_patients(request):
    context = {
        'patients': Enrollment.objects.all()
    }
    return render(request, 'patients/patients_list.html', context)


def all_doctors(request):
    context = {
        'doctors': DoctorProfile.objects.all()
    }
    return render(request, 'patients/doctors_list.html', context)