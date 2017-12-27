"""
Unit test our blog app.

Note: Django's Test Client already tests for URL resolution, which
means we don't need to test for this. YAYYYY!!!
"""

import unittest
from unittest.mock import patch
from datetime import datetime
from pytz import utc

from django.test import TestCase
from django.http import HttpRequest
from django.core.exceptions import ValidationError

from blog.views import home_page
from blog.models import Article


def create_articles(num_articles: int):
    """
    Create specified number of published articles in database.
    """
    articles_created = 0
    while articles_created < num_articles:
        Article.objects.create(published=True)
        articles_created += 1


class HomePageViewTest(unittest.TestCase):
    """
    Suite of unit tests that test our Home page view.
    """

    @patch('blog.views.Article')
    def test_gets_article_data(self, mock_article):
        """
        Test that the view gets published article data.
        """
        request = HttpRequest()
        home_page(request)
        mock_article.get_articles.assert_called_once_with(page=1)

    @patch('blog.views.Article')
    @patch('blog.views.render')
    def test_renders_html(self, mock_render, mock_article):
        """
        Test that the view renders the home HTML with the associated
        post data.
        """
        request = HttpRequest()
        response = home_page(request)
        self.assertEqual(response, mock_render.return_value)
        mock_render.assert_called_once_with(
            request,
            'home.html',
            {'article': mock_article.get_articles()}
        )


class ArticleModelTest(TestCase):
    """
    Suite of unit tests that test the article model.
    """

    def test_article_has_title(self):
        """
        Test that an article must have an associated title.
        """
        article = Article(title='')
        with self.assertRaises(ValidationError):
            article.save()
            article.full_clean()

    def test_has_body(self):
        """
        Test that an article must have an associated body.
        """
        article = Article(body='')
        with self.assertRaises(ValidationError):
            article.save()
            article.full_clean()

    def test_date_is_current_datetime(self):
        """
        Test that an article must have a datetime associated with it
        that is by default the current UTC time.
        """
        current_datetime = utc.localize(datetime.utcnow())
        article = Article()
        time_difference = article.date - current_datetime
        self.assertAlmostEqual(time_difference.total_seconds(), 0, places=2)

    def test_published_is_false_by_default(self):
        """
        Test that articles have a boolean "published" field which is
        false by default.
        """
        article = Article()
        self.assertEqual(False, article.published)


class GetArticlesTest(TestCase):
    """
    Suite of unit tests that test the get_articles model method.
    """

    def test_returns_published_articles(self):
        """
        Test that the Article model has a get_articles method that
        returns published articles.
        """
        article = Article.objects.create(published=True)
        self.assertEqual(article, Article.get_articles()[0])

    def test_doesnt_return_unpublished(self):
        """
        Test that only published articles are returned, and unpublished
        articles are left out.
        """
        published_article = Article.objects.create(published=True)
        Article.objects.create(published=False)
        self.assertEqual(len(Article.get_articles()), 1)
        self.assertEqual(published_article, Article.get_articles()[0])

    def test_returns_ten_articles(self):
        """
        Test that a maximum of 10 articles are returned.
        """
        create_articles(11)
        self.assertEqual(len(Article.get_articles()), 10)

    def test_order_by_published_date(self):
        """
        Test that the articles returned are ordered by published date
        descending.
        """
        create_articles(10)
        dates = []
        for article in Article.get_articles():
            dates.append(article.date)
        dates_diff = [i - j for i, j in zip(dates[:-1], dates[1:])]
        dates_diff_is_positive = [i.total_seconds() > 0 for i in dates_diff]
        self.assertTrue(all(dates_diff_is_positive))

    def test_pagination(self):
        """
        Test that articles are returned in pages, with the first page
        containing the most recent articles.
        """
        create_articles(11)
        second_article = Article.get_articles(page=1)[9]
        first_article = Article.get_articles(page=2)[0]
        self.assertEqual(second_article.id, 2)
        self.assertEqual(first_article.id, 1)

    def test_first_page_default(self):
        """
        Test that the first page is returned by default.
        """
        create_articles(11)
        self.assertEqual(Article.get_articles()[0], Article.get_articles(page=1)[0])
