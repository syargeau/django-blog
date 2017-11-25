"""
Unit test our blog app.
"""

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from blog.views import home_page

class SmokeTest(TestCase):
    """
    Deliberately failing test to initiate our testing.
    """

    def test_root_url_resolves_home(self):
        """
        Test that the root URL resolves to the home page.
        """
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_response(self):
        """
        Test that the home page is returning a successful HTTP response.
        """
        request = HttpRequest()
        response = home_page(request)
        self.assertEqual(response.status_code, 200)
