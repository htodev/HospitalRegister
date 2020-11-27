from django.urls import path
from .views import all_patients, all_doctors

urlpatterns = [
    path('', all_patients, name='all-patients'),
    path('doctors/', all_doctors, name='all-doctors'),
]