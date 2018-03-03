"""
End to end functional tests that test the integration of the home page
from the users viewpoint.
"""

from django.test import LiveServerTestCase
from selenium import webdriver

from blog.models import Article


class BasicHomePageTest(LiveServerTestCase):
    """
    Tests that we can get a basic home page up and running.
    """

    @classmethod
    def setUpClass(cls):
        """
        Initiate the whole testing suite by adding articles to the
        testing database.
        """
        super().setUpClass()
        num_articles = 11
        for article in range(1, (num_articles + 1)):
            Article.objects.create(
                title=f'Test Article {article}',
                body=f'Test body content {article}',
                published=True
            )

    def setUp(self):
        """
        Initiate every test by setting up the browser.
        """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        Stop every test by quitting the browser.
        """
        self.browser.quit()

    def test_load_home_page(self):
        """
        Test that the home page loads as expected (i.e. with
        title and header).
        """
        self.browser.get(self.live_server_url)
        # Bob logs into Django Blog, the best Django blog engine ever! He notices it's title.
        desired_title = 'Django Blog'
        self.assertEqual(self.browser.title, desired_title)
        # Bob sees 10 articles
        articles = self.browser.find_elements_by_class_name('article')
        self.assertEqual(len(articles), 10)
        # He notices the titles of them correspond to the most recent articles in
        # descending date order.
        # Note: in our test case, these articles are given the numbered titles 1-11,
        # so the most recent ones will be 2-11, with 11 being the first.
        for article, article_number in zip(articles, range(11, 1, -1)):
            expected_title = f'Test Article {article_number}'
            self.assertEqual(article.text, expected_title)

    def test_pagination(self):
        """
        Test for a button to click on next 10 articles, and ensure
        that this loads the next 10 articles with the proper URL.
        """
        self.browser.get(self.live_server_url)
        # Bob notices a button to go to the "next" page
        next_button = self.browser.find_element_by_id('next-page-button')
        self.assertEqual(next_button.text, 'Next Page')
        # He clicks the button, and it loads the next most recent articles
        
        # This time, he notices a button to go to both the "previous" and "next" page

        # He goes the final page, and notices the "next" option is no longer present

        # Continue testing...
        self.fail('Finish all tests first!')
