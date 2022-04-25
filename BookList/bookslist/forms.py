from django import forms
from .models import Book


class CreateBook(forms.ModelForm):
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


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = ('title',
                  'author',
                  'publish',
                  'isbn_number',
                  'number_of_pages',
                  'cover_link',
                  'publication_language')


