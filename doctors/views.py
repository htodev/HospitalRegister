from django.shortcuts import render
from django.views import generic
from doctors.models import Doctors
# Create your views here.


class DoctorsList(generic.ListView):

    model = Doctors
    template_name = 'doctors_list.html'
    context_object_name = 'doctors'