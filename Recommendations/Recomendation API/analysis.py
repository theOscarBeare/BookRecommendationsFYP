from Recommendations.models import enduser
from DataCall.models import Books
import psycopg2


def enduserBooksRead(self, enduserID=1):
    enduser.objects.filter(enduserID=enduserID)
    booksReadID = enduser.execute("select bookidread from userinfomation WHERE enduserid = enduserID")
    [] = Books.execute("select * from Books WHERE bookid = booksReadID")

    return []

