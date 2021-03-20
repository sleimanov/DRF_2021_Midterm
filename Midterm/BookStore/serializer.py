from rest_framework import serializers
from BookStore.models import BookJournalBase, Book, Journal

class BookSerializer(serializers.ModelSerializer):
    class Mets:
        fields = (
            'name',
            'price',
            'description',
            'created_at',
            'num_pages',
            'genre'
        )
        model = Book


class JournalSerializer(serializers.ModelSerializer):
    class Mets:
        fields = (
            'name',
            'price',
            'description',
            'created_at',
            'type',
            'publisher'
        )
        model = Journal