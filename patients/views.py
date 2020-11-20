from django.shortcuts import render

from enrollment_system.models import Enrollment


def all_patients(request):
    context = {
        'patients': Enrollment.objects.all()
    }
    return render(request, 'patients/patients_list.html', context)