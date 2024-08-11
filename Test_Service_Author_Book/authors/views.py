from django.shortcuts import render, redirect
from django.views import View

from books.models import Book
from .forms import AuthorForm
from .models import Author


class AuthorFormCreateView(View):  # добавление автора в БД
    def get(self, request):
        form = AuthorForm()
        return render(request, 'authors/create2.html',
                      {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/authors')
        return render(request, 'authors/create2.html',
                      {'form': form})


class AuthorFormEditView(View):  # Редактирование автора по id
    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('id')
        author = Author.objects.get(id=author_id)
        form = AuthorForm(instance=author)
        return render(request, 'authors/update.html',
                      {'form': form, 'author_id': author_id})

    def post(self, request, *args, **kwargs):
        author_id = kwargs.get('id')
        author = Author.objects.get(id=author_id)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('/authors')
        return render(request, 'authors/update.html',
                      {'form': form, 'author_id': author_id
                       })


class AuthorFormFindBookView(View):  # поиск книг по автору в БД
    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('id')
        author = Author.objects.get(pk=author_id)
        books = Book.objects.filter(fk_book_to_author=author_id)
        return render(request, 'books/show_all_find_author.html', context={
            'books': books, 'author_name': author.name
        })


class AuthorAllView(View):  # просмотр всех авторов из БД
    def get(self, request):
        authors = Author.objects.all()[:35]
        return render(request, 'authors/show_all.html', context={
            'authors': authors,
        })


class AuthorView(View):  # просмотр автора из БД по id
    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('author_id')
        author = Author.objects.get(pk=author_id)
        return render(request, 'authors/show.html', context={
            'author': author,
        })


class AuthorFormDeleteView(View):  # Удаление автора из БД по ID
    def post(self, *args, **kwargs):
        author_id = kwargs.get('author_id')
        author = Author.objects.get(id=author_id)
        if author:
            author.delete()
        return redirect('/authors')


class AuthorAllFormDeleteView(View):  # Удаление всех авторов из БД.
    def post(self, *args, **kwargs):
        author = Author.objects.all()
        if author:
            author.delete()
        return redirect('/authors')
