from django.urls import path

from .views import (BookFormCreateView, BookAllView, BookView, BookFormDeleteView, BookAllFormDeleteView,
                    BookFormEditView, BookFormFindView, BookFormFindAuthorView, BookFormFindBookView)

app_name = 'book'

urlpatterns = [
    path('create/', BookFormCreateView.as_view(), name='book_create'),  # добавление книги в БД
    path('edit/<int:id>/', BookFormEditView.as_view(), name='book_update'),  # редактирование книги в БД по id
    path('find/', BookFormFindView.as_view(), name='book_find'),  # поиск книг в БД
    path('find_author/', BookFormFindAuthorView.as_view(), name='book_find_author'),  # поиск книг по имени автора в БД
    path('find_book/', BookFormFindBookView.as_view(), name='book_find_book'),  # поиск книг по названию в БД
    path('<book_id>/', BookView.as_view(), name='BookView'),  # просмотр книги из БД по id
    path('del/all/', BookAllFormDeleteView.as_view(), name='book_all_del'),  # удаление всех книг из БД
    path('del/<int:book_id>/', BookFormDeleteView.as_view(), name='book_del'),  # удаление книги из БД по ID
    path('', BookAllView.as_view(), name='BookAllView')  # просмотр всех книг из БД

]
