"""This module contains functions about retrieving of patients names,
 doctors names from Enrollment object, and lists all Enrollments connected
 to certain doctor(its owner). """

from django.shortcuts import render
from enrollment_system.models import Enrollment
from doctors_auth.models import DoctorProfile
from .forms import PatientFilterForm, DoctorFilterForm


def extract_filter_values(values):
    """It takes request param 'text' and returns its value"""
    text = values['text'] if 'text' in values else ''
    return text


def all_patients(request):
    """It retrieves patients names form Enrollments records. """

    text = extract_filter_values(request.GET)
    patient = Enrollment.objects.filter(patient_name__contains=text)
    context = {
        'patients': patient,
        'patient_filter_form': PatientFilterForm(initial={'text': text})
    }
    return render(request, 'hospital_units/patients_list.html', context)


def all_doctors(request):
    """It retrieves doctors names from DoctorProfile records. """

    text = extract_filter_values(request.GET)
    doctor = DoctorProfile.objects.filter(name__contains=text)
    context = {
        'doctors': doctor,
        'doctor_filter_form': DoctorFilterForm(initial={'text': text})
    }
    return render(request, 'hospital_units/doctors_list.html', context)


def doctors_records(request):
    """It filters Enrollment records by their owners. """

    context = {
        'enrollments': Enrollment.objects.filter(doctor_name_id=request.user.doctorprofile.id)
    }
    return render(request, 'hospital_units/doctors_enrollments.html', context)
