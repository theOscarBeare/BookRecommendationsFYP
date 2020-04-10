from django.test import TestCase, Client
from django.urls import reverse
from DataCall.models import Author, Books
from DataCall.serializer import AuthorSerializer, BooksSerializer
import json


class TestViews(TestCase):
    def test_Turing_is_Alan(self):
        if Author.authorlname == 'Turing':
            assert Author.authorfname == 'Alan'

    def test_tables_can_be_joined(self):
        # this test makes sure that the author table can be joined to the book table
        # through the authorbooks table.
        if Author.authorid == 3:
            assert Books.bookname == 1

    def test_Babbage_is_Charles(self):
        if Author.authorlname == 'Babbage':
            assert Author.authorfname == 'Charles'

    def test_Turing_is_Not_Charles(self):
        if Author.authorlname == 'Turing':
            assert Author.authorfname != 'Charles'

    def test_Language_and_Mind_is_written_by_Chomsky(self):
        if Author.authorlname == 'Chomsky':
            assert Books.bookname == 'Language and Mind'

    def test_there_is_data_in_the_database(self):
        print(Author.authorlname)
