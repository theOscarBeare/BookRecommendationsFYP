from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import *
from .serializer import *


class AllAuthor(ListAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorView(APIView):

    def get(self, request, pk, format=None):
        try:
            tech = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(tech)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tech = Author.objects.get(pk=pk)
        tech.delete()
        return Response(status=status.HTTP_200_OK)


class AllBooks(ListAPIView):

    queryset = Author.objects.all()
    serializer_class = BooksSerializer

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BooksView(APIView):

    def get(self, request, pk, format=None):
        try:
            tech = Books.objects.get(pk=pk)
            serializer = BooksSerializer(tech)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tech = Books.objects.get(pk=pk)
        tech.delete()
        return Response(status=status.HTTP_200_OK)