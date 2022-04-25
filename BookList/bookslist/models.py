from django.db import models
from django.utils import timezone


class Book(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.CharField(max_length=200)
    publish = models.DateField(default=timezone.now)
    isbn_number = models.PositiveBigIntegerField()
    number_of_pages = models.PositiveIntegerField()
    cover_link = models.URLField(max_length=200, blank=True)
    publication_language = models.CharField(max_length=200)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title
