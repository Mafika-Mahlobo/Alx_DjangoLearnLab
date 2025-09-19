from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r"book_all", views.BookViewSet, basename="book_all")


urlpatterns = [
	path("books/", views.BookList.as_view(), name="book-list"),
	path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
	path("", include(router.urls)),
]