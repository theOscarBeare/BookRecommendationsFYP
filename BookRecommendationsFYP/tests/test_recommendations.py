from django.test import TestCase
from django.urls import resolve, reverse
from DataCall.models import Author, Books
from Recommendations.models import *
from Recommendations.Recomendation_API.RecomendationGenerator import *


class TestRecommendations(TestCase):

    def test_Books_Viewed_Not_Equal_To_Books_Read(self):
        Viewed, Read = updateRecommendations()

        for i in Viewed:
            if i not in Read:
                continue
            else:
                TestCase.fail(self)

    def test_Books_Read_Not_Equal_To_Books_Viewed(self):
        Viewed, Read, Reviewed = updateRecommendations()

        for i in Read:
            if i not in Viewed:
                continue
            else:
                TestCase.fail(self)

    def test_Books_Viewed_Not_Equal_To_Books_Reviewed(self):
        Viewed, Read, Reviewed = updateRecommendations()

        for i in Viewed:
            if i not in Reviewed:
                continue
            else:
                TestCase.fail(self)

    def test_recommendations_updated(self):
        oldRecommendationsList = userrecommendations.execute("select * from userrecommendations;")
        updateRecommendations()
        newRecommendationsList = userrecommendations.execute("select * from userrecommendations;")
        if oldRecommendationsList == newRecommendationsList:
            TestCase.fail(self)
        else:
            pass
