from django.urls import path, include
from . import views

urlpatterns = [
	path("api/register/", views.RegisterAPIView.as_view(), name="register"),
	path("login/", views.LoginView.as_view(), name="login"),
	path("profile/", views.ProfileView.as_view(), name="profile"),
]