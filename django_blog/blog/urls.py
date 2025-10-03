from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path("register/", views.register_view, name="register"),
	path("profile/", views.home_view, name="home"),
	path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
	path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]