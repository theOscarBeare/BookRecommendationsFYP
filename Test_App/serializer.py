from rest_framework import serializers
from .models import Author
from .models import Books
from .models import Authorbooks
from .models import Reviews


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'


class AuthorBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authorbooks
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'