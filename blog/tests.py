"""
Unit test our blog app.

Note: Django's Test Clien already tests for URL resolution among other things,
which means we don't need to test for super simple exceptions such as that.
"""

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from blog.views import home_page

class HomePageView(TestCase):
    """
    Suite of unit tests that test our Home page view.
    """

    def test_home_uses_correct_html(self):
        """
        Test that the home page is rendering the correct HTML template.
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
