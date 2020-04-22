from Recommendations.models import enduser
from DataCall.models import Books
import psycopg2

BooksList = []
reviewedList = []
booksViewed = []


def setEnduserBooksRead(enduserID):
    global BooksList
    enduser.objects.filter(enduserID=enduserID)
    booksReadID = enduser.execute("select bookidread from public.userinformation WHERE userid = enduserID and;")
    for i in booksReadID:
        booksReadID = booksReadID[i]
        [BooksList] = Books.execute("select * from public.Books WHERE bookid = booksReadID;")

    return [BooksList]


def setEndUserBooksReviewed(enduserID):
    global reviewedList
    enduser.objects.filter(enduserID=enduserID)
    booksReviewedID = enduser.execute("select bookidreviewed from public.userinformation where userid = enduserID;")
    for i in booksReviewedID:
        bookReviewedID = booksReviewedID[i]
        [reviewedList] = Books.execute("select * from public.Books where bookidreviewed = booksReviewedID;")

    return [reviewedList]


def setEnduserKnowledgeScore(enduserID):
    enduser.objects.filter(enduserID=enduserID)
    enduserKnowledge = enduser.execute("select userknowledgelevel from public.userinformation where userid = enduserID;")

    return enduserKnowledge


def setEnduserBooksViewed(enduserID):
    global booksViewed
    enduser.objects.filter(enduserID=enduserID)
    booksViewedID = enduser.execute("select bookidviewed from public.userinformation where userid = enduserID;")
    for i in booksViewedID:
        bookViewedID = booksViewedID
        [booksViewed] = Books.execute("select * from Books WHERE bookid = booksViewedID;")

    return [booksViewed]
