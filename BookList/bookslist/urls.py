from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create_book/', views.create_book, name='create_book'),
    path('book/<id>/', views.curent_book, name='curent_book'),
    path('edit_book/<int:pk>/', views.edit, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete, name='delete_book'),
]

