from django.contrib import admin
from.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'isbn_number', 'number_of_pages')
    list_filter = ('author', 'publish', 'publication_language', 'isbn_number')
    prepopulated_fields = {'slug': ('title',)}

