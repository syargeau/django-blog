"""
These functions govern how HTTP requests are rendered! Woohoo... this is the meat.
"""

from django.shortcuts import render


def home_page(request):
    """
    Renders the view for our home page.
    """
    return render(request, 'home.html')
