from django.views import generic
from .models import Doctors
from .forms import DoctorForms


class DoctorsList(generic.ListView):

    model = Doctors
    template_name = 'doctors/doctors_list.html'
    context_object_name = 'doctors'


class DoctorDetail(generic.DetailView):
    model = Doctors
    template_name = 'doctors/doctor_detail.html'
    context_object_name = 'doctor'


class DoctorCreate(generic.CreateView):
    model = Doctors
    form_class = DoctorForms
    template_name = 'doctors/doctor_create.html'
    success_url = '/doctors'


class DoctorsUpdate(generic.UpdateView):
    model = Doctors
    template_name = 'doctors/doctor_create.html'
    form_class = DoctorForms
    success_url = '/doctors'


class DeleteDoctor(generic.DeleteView):
    model = Doctors
    template_name = 'doctors/doctor_delete.html'
    success_url = '/doctors'


