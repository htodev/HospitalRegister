from django.shortcuts import render
from enrollment_system.models import Enrollment
from doctors_auth.models import DoctorProfile
from .forms import PatientFilterForm, DoctorFilterForm


def extract_filter_values(values):
    text = values['text'] if 'text' in values else ''
    return text


def all_patients(request):

    text = extract_filter_values(request.GET)
    patient = Enrollment.objects.filter(patient_name__contains=text)
    context = {
        'patients': patient,
        'patient_filter_form': PatientFilterForm(initial={'text': text})
    }
    return render(request, 'hospital_units/patients_list.html', context)


def all_doctors(request):
    text = extract_filter_values(request.GET)
    doctor = DoctorProfile.objects.filter(name__contains=text)
    context = {
        'doctors': doctor,
        'doctor_filter_form': DoctorFilterForm(initial={'text': text})
    }
    return render(request, 'hospital_units/doctors_list.html', context)


def doctors_records(request):
    context = {
        'enrollments': Enrollment.objects.filter(doctor_name_id=request.user.doctorprofile.id)
    }
    return render(request, 'hospital_units/doctors_enrollments.html', context)
