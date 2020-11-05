from django.shortcuts import render
from django.views import generic
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def redirect_to_user_profile(request):
    url = f'/accounts/profile/{request.user.id}/'
    return HttpResponsePermanentRedirect(redirect_to=url)


class UserProfileDetail(generic.DeleteView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'useer'


class SignUp(generic.CreateView):
    # model = User
    form_class = UserCreationForm
    success_url = '/accounts/login'
    template_name = 'register.html'