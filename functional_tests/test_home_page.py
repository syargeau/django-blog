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
        Test that the home page loads as expected (i.e. with title and header).
        """
        self.browser.get(self.live_server_url)
        # Bob logs into Moto Now Blog, the best site ever! He notices it's title.
        desired_title = 'Moto Now Blog'
        self.assertEqual(self.browser.title, desired_title)
        # Bob sees the title of the 10 most recent posts on the home page.
        # Note: in our test case, these articles are given the numbered titles 1-11,
        # so the most recent ones will be 2-11.
        page_text = self.browser.find_element_by_tag_name('body').text
        for article in range(2, 12):
            self.assertIn(f'Test Article {article}', page_text)
        self.assertNotIn('Test Article 1', page_text)
        # Continue testing...
        self.fail('Finish all tests first!')
