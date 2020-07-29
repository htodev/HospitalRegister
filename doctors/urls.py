from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.DoctorsList.as_view(), name='doctors')
]