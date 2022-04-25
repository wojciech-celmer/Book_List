from rest_framework import serializers
from bookslist.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title',
                  'author',
                  'slug',
                  'publish',
                  'isbn_number',
                  'number_of_pages',
                  'cover_link',
                  'publication_language')
