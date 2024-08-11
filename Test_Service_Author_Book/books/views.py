from django.shortcuts import render, redirect
from django.views import View

from authors.models import Author
from .forms import BookForm
from .models import Book


class BookFormCreateView(View):    # добавление книги в БД
    def get(self, request):
        form = BookForm()
        return render(request, 'books/create2.html',
                      {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')
        return render(request, 'books/create2.html', {'form': form})


class BookFormEditView(View):  # редактирование записи с книгой в БД
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        book = Book.objects.get(id=book_id)
        book2 = Book.objects.get(pk=book_id)
        form = BookForm(instance=book)
        return render(request, 'books/update.html', {'form': form, 'book2': book2, 'book_id': book_id})

    def post(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        book = Book.objects.get(id=book_id)
        book2 = Book.objects.get(pk=book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books')
        return render(request, 'books/update.html',
                      {'form': form, 'book2': book2, 'book_id': book_id})


class BookAllView(View):  # просмотр всех книг из БД
    def get(self, request):
        books = Book.objects.all()[:35]
        return render(request, 'books/show_all.html', {'books': books})


class BookView(View):  # просмотр книги из БД по id
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        book = Book.objects.get(pk=book_id)
        return render(request, 'books/show.html', context={
            'book': book,
        })


class BookFormFindView(View):  # поиск книги в БД
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/find.html', context={
            'books': books,
        })


class BookFormFindAuthorView(View):  # поиск книги по автору в БД
    def get(self, request):
        find_author = request.GET.get('find_text', "Имя автора")
        author = Author.objects.get(name=find_author)
        books = Book.objects.filter(fk_book_to_author=author.id)
        return render(request, 'books/show_all_find_author.html', context={
            'books': books, 'author_name': find_author
        })


class BookFormFindBookView(View):  # поиск книги по названию в БД
    def get(self, request):
        find_book = request.GET.get('find_text', "Название книги")
        books = Book.objects.filter(title=find_book)
        return render(request, 'books/show_all.html', context={
            'books': books,
        })


class BookFormDeleteView(View):  # удаление книги по ID
    def post(self, *args, **kwargs):
        book_id = kwargs.get('book_id')
        book = Book.objects.get(id=book_id)
        if book:
            book.delete()
        return redirect('/books')


class BookAllFormDeleteView(View):  # удаление всех книг в БД
    def post(self, *args, **kwargs):
        book = Book.objects.all()
        if book:
            book.delete()
        return redirect('/books')
