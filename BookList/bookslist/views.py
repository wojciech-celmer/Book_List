from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import CreateBook, BookEditForm#, BookDeleteForm
from django.shortcuts import redirect
from .filters import BookFilter
from django.views.generic import ListView, DeleteView


def book_list(request):
    books = Book.objects.all()

    my_filter = BookFilter(request.GET, queryset=books)
    books = my_filter.qs

    context = {'books': books, 'my_filter': my_filter}
    return render(request, 'BookList/bookslist/list.html', context)


class BookList(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookListFilter(self.request.GET, queryset=self.get_queryset())
        return context



def curent_book(request, id):
    book_detail = Book.objects.get(pk=id)
    return render(request, 'BookList/bookslist/book_detail.html', {'book_detail': book_detail})


def create_book(request):
    if request.method == "POST":
        form = CreateBook(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('book_list')
    else:
        form = CreateBook()
    return render(request, 'BookList/bookslist/create_book.html', {'form': form})


def edit(request, pk):
    post = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('book_list')
    else:
        form = BookEditForm(instance=post)
    return render(request, 'BookList/bookslist/edit.html', {'form': form})


def delete(DeleteView, pk):

    if DeleteView.method == "POST":
        bk = Book.objects.get(id=pk)
        bk.delete()
        return redirect('book_list')

    return render(DeleteView, 'BookList/bookslist/delete.html')