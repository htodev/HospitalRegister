"""This module contains generic CBV which provide
create, get, update, delete and list functionality
for Enrollment model. """

from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Enrollment
from.forms import EnrollmentForm


class EnrollmentCreate(generic.CreateView):
    """It contains create functionality. """

    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_create.html'
    success_url = '/enrollments'


class EnrollmentList(generic.ListView):
    """It contains list functionality. """

    model = Enrollment
    template_name = 'enrollments/enrollment_list.html'
    context_object_name = 'enrollments'


class EnrollmentDetail(generic.DetailView):
    """It contains get functionality. """

    model = Enrollment
    template_name = 'enrollments/enrollment_detail.html'
    context_object_name = 'enrollment'

    def get(self, request, *args, **kwargs):
        """This method overrides built-in 'get' function and forbid to users which are
         not owners to Enrollment object to receive access to it. """

        obj = get_object_or_404(self.model, pk=kwargs['pk'])
        if request.user.doctorprofile.name != str(obj.doctor_name):
            raise PermissionDenied
        return super().get(request, *args, **kwargs)


class EnrollmentUpdate(generic.UpdateView):
    """It contains update functionality. """

    model = Enrollment
    template_name = 'enrollments/enrollment_create.html'
    form_class = EnrollmentForm
    success_url = '/enrollments'


class EnrollmentDelete(generic.DeleteView):
    """It contains delete functionality. """

    model = Enrollment
    template_name = 'enrollments/enrollment_delete.html'
    success_url = '/enrollments'
