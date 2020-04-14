from .analysis import enduserBooksRead
from DataCall.models import *
from Recommendations.models import userrecommendations
import psycopg2


def gatherEndUserInformation():
    listOfReadBooks = enduserBooksRead(1)
    for i in listOfReadBooks:
        book = listOfReadBooks[i]
        BookRead = Books.execute("select book from Books")
        return BookRead


def updateRecommendations():
    BookRead = gatherEndUserInformation()
    userrecommendations.execute("UPDATE userrecommendations ")


