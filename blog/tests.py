"""
Unit test our blog app.
"""

from django.test import TestCase
from django.urls import resolve
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
