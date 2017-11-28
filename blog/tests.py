"""
Unit test our blog app.

Note: Django's Test Client already tests for URL resolution, which means
we don't need to test for this. YAYYYY!!!
"""

from unittest.mock import patch
from django.test import TestCase
from django.http import HttpRequest
from blog.views import home_page


class HomePageViewTest(TestCase):
    """
    Suite of unit tests that test our Home page view.
    """

    @patch('blog.views.Article')
    def test_gets_post_data(self, mock_article):
        """
        Test that the view gets published article data.
        """
        request = HttpRequest()
        home_page(request)
        mock_article.objects.get.assert_called_once_with(published=True)

    @patch('blog.views.Article')
    @patch('blog.views.render')
    def test_renders_html(self, mock_render, mock_article):
        """
        Test that the view renders the home HTML with the associated post data.
        """
        request = HttpRequest()
        response = home_page(request)
        self.assertEqual(response, mock_render.return_value)
        mock_render.assert_called_once_with(
            request,
            'home.html',
            {'article': mock_article.objects.get()}
        )
