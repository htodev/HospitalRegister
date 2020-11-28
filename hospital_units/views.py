from django.shortcuts import render

from enrollment_system.models import Enrollment
from doctors_auth.models import DoctorProfile


def all_patients(request):
    context = {
        'patients': Enrollment.objects.all()
    }
    return render(request, 'hospital_units/patients_list.html', context)


def all_doctors(request):
    context = {
        'doctors': DoctorProfile.objects.all()
    }
    return render(request, 'hospital_units/doctors_list.html', context)


def doctors_records(request):
    doctor = DoctorProfile.objects.get(user_id=request.user.id)
    query = Enrollment.objects.filter(doctor_name_id=doctor.id)
    context = {
        'records': query
    }
    return render(request, 'hospital_units/doctors_enrollments.html', context)
