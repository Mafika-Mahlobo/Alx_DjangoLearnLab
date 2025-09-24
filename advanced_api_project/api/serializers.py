from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """"
    Serializes book data into JSON. Check if publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        if data["publication_year"] > 2025:
            raise serializers.ValidationError("Publication year cannot be ib the future!")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    """
    Author serializer with nested book serializer.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]