from django.urls import path

from .views import (AuthorFormCreateView, AuthorAllView, AuthorView, AuthorFormDeleteView, AuthorAllFormDeleteView,
                    AuthorFormEditView, AuthorFormFindBookView)

app_name = 'author'

urlpatterns = [
    path('create/', AuthorFormCreateView.as_view(), name='author_create'),  # добавление автора в БД
    path('edit/<int:id>/', AuthorFormEditView.as_view(), name='author_update'),  # редактирование автора в БД по ID
    path('find/<int:id>/', AuthorFormFindBookView.as_view(), name='author_find_book'),  # поиск всех книг автора в БД
    path('<author_id>/', AuthorView.as_view(), name='AuthorView'),  # просмотр автора из БД по id
    path('del/all/', AuthorAllFormDeleteView.as_view(), name='author_all_del'),  # удаление всех авторов из БД
    path('del/<int:author_id>/', AuthorFormDeleteView.as_view(), name='author_del'),  # удаление автора из БД по ID
    path('', AuthorAllView.as_view(), name='AuthorAllView')  # просмотр всех авторов из БД

]
