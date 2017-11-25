"""
These functions govern how HTTP requests are rendered! Woohoo... this is the meat.
"""

from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    """
    Renders the view for our home page.
    """
    return HttpResponse()
