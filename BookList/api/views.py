from rest_framework import filters
from rest_framework import generics
from bookslist.models import Book
from .serializers import BookSerializer
from django.shortcuts import render, redirect
import requests



class BookListApi(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'publication_language', 'publish']


# def book_search(request, query):
#     key = 'AIzaSyC9NZnC9YBdxM3L5XTxLuUP2QQ-I4j_eJY'
#     response = requests.get('https://www.googleapis.com/books/v1/volumes?q='+ query +'&key='+ key).json()
#     return render(request, 'book_search.html', {'response': response})

def book_search(request):
    key = 'AIzaSyC9NZnC9YBdxM3L5XTxLuUP2QQ-I4j_eJY'
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=harry&key='+ key).json()
    return render(request, 'book_search.html', {'response': response})


