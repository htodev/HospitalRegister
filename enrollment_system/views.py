from django.views import generic
from .models import Enrollment
from.forms import EnrollmentForm


class EnrollmentCreate(generic.CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_create.html'
    success_url = '/enrollments'


class EnrollmentList(generic.ListView):

    model = Enrollment
    template_name = 'enrollments/enrollment_list.html'
    context_object_name = 'enrollments'


class EnrollmentDetail(generic.DetailView):
    model = Enrollment
    template_name = 'enrollments/enrollment_detail.html'
    context_object_name = 'enrollment'


class EnrollmentUpdate(generic.UpdateView):
    model = Enrollment
    template_name = 'enrollments/enrollment_create.html'
    form_class = EnrollmentForm
    success_url = '/enrollments'


class EnrollmentDelete(generic.DeleteView):
    model = Enrollment
    template_name = 'enrollments/enrollment_delete.html'
    success_url = '/enrollments'
