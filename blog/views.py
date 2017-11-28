"""
These functions govern how HTTP requests are rendered! Woohoo... this is the meat.
"""

from django.shortcuts import render
from blog.models import Article


def home_page(request):
    """
    Renders the view for our home page.
    """
    article = Article.objects.get(published=True)
    return render(request, 'home.html', {'article': article})
