from .analysis import setEnduserBooksRead, setEnduserBooksViewed, setEnduserKnowledgeScore, setEndUserBooksReviewed
from DataCall.models import *
from Recommendations.models import userrecommendations
import psycopg2

enduserID = 1
BooksRead = []
BooksReviewed = []
BooksViewed = []


def getEndUserInformationBooksRead():
    global BooksRead
    listOfReadBooks = setEnduserBooksRead(enduserID)
    for i in listOfReadBooks:
        book = listOfReadBooks[i]
        [BooksRead] = Books.execute("select book from public.Books;")

    return [BooksRead]


def getEndUserInformationBooksReviewed():
    global BooksReviewed
    listOfBooksReviewed = setEndUserBooksReviewed(enduserID)
    for i in listOfBooksReviewed:
        book = listOfBooksReviewed[i]
        [BooksReviewed] = Books.execute("select book from public.Books;")

    return [BooksReviewed]


def getEndUserInformationBooksViewed():
    global BooksViewed
    listOfViewedBooks = setEnduserBooksViewed(enduserID)
    for i in listOfViewedBooks:
        book = listOfViewedBooks[i]
        [BooksViewed] = Books.execute("select book from public.Books;")

    return [BooksViewed]


def getEndUserKnowledge():
    endUserKnowledgeLevel = setEnduserKnowledgeScore(enduserID)
    return endUserKnowledgeLevel


def updateRecommendations():
    BookRead = getEndUserInformationBooksRead()
    BookViewed = getEndUserInformationBooksViewed()
    BookReviewed = getEndUserInformationBooksReviewed()
    endUserKnowledgeLevel = getEndUserKnowledge()

    for i in BookViewed:
        if i in BookRead:
            BookViewed.pop(i)
            i = i-1
        elif i in BookReviewed:
            BookViewed.pop(i)
            i = i-1

    for i in BooksViewed:
        bookDifficulty = Books.execute("select bookdifficulty from public.Books where BookName = BooksViewed[i];")
        if bookDifficulty != endUserKnowledgeLevel:
            BooksViewed.pop(i)
            i = i-1

    for i in BookViewed:
        viewed = BookViewed[i]
        userrecommendations.execute("INSERT INTO public.userrecommendations (userID, bookid) VALUES (enduserID, "
                                    "viewed);")

# These returns are for testing and make no difference to the program
    return BookRead, BookViewed, BooksReviewed


