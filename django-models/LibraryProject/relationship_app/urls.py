from .views import list_books, LibraryDetailView, user_registration, logout_view
from django.urls import path

urlpatterns = [
    path("books/", list_books, name="books"),
    path("library/", LibraryDetailView.as_view(), name="library"),
    path("register/", user_registration, name="register"),
    path("logout/", logout_view, name="logout"),

]