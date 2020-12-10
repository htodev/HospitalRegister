"""The 'urlpatterns' list routesURLs to views."""

from django.urls import path
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing-page')
]
