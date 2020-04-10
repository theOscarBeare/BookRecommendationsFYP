from django.test import SimpleTestCase
from django.urls import resolve, reverse
from BookRecommendationsFYP.view import index, FrontendAppView
from DataCall.views import AllAuthor, AuthorView, AllBooks, BooksView


class TestsUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        pass