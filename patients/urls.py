from django.urls import path
from .views import all_patients

urlpatterns = [
    path('', all_patients, name='all-patients')
]