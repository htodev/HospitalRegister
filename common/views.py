"""Module which provides landing page."""

from django.shortcuts import render


def landing_page(request):
    """This function provide landing page fro the project."""

    return render(request, 'landing_page.html')
