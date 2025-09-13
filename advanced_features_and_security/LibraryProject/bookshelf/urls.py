from django.urls import path
from .views import book_list_view, book_add_view, book_edit_view, book_delete_view

urlpatterns = [

	path("books/view", book_list_view, name="book_list"),
	path("books/add", book_add_view, name="book_add"),
	path("books/edit", book_edit_view, name="book_edit"),
	path("books/delete", book_delete_view, name="book_delete"),
]