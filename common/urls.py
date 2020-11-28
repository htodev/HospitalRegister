from django.urls import path
from .views import landing_page, doctor_profile_landing_page

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('profile/', doctor_profile_landing_page, name='doctor profile')
]
