"""
Define models for the blog functionality.
"""

from django.db import models
from django.utils.timezone import now


class Article(models.Model):
    """
    Handles all article related data. Available properties are title,
    body, date, and published.
    """
    title = models.CharField(max_length=200, default='', blank=False)
    body = models.TextField(default='', blank=False)
    date = models.DateTimeField(default=now, blank=False)
    published = models.BooleanField(default=False)

    objects = models.Manager()  # to prevent pylint E1101; force recognize objects member

    @staticmethod
    def get_articles(page: int = 1):
        """
        Return the published articles that belong to the specified page
        of the blog.
        """
        num_articles_per_page = 10
        first_article = (page-1) * num_articles_per_page
        last_article = page * num_articles_per_page
        published_articles = Article.objects.filter(published=True).order_by('-date')
        return published_articles[first_article:last_article]
