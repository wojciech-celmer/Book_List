from django.urls import path
from .views import BookListApi, book_search

urlpatterns = [
    path('', BookListApi.as_view(), name='book_list_view'),
    path('search/', book_search, name='book_search')
]