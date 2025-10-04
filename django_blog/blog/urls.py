from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path("register/", views.register_view, name="register"),
	path("profile/", views.home_view, name="home"),
	path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
	path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
	path("posts/", views.ListPostsView.as_view(), name="posts"),
	path("post/new/", views.CreatePostView.as_view(), name="create"),
	path("post/<int:pk>/update/", views.EditPostView.as_view(), name="edit"),
	path("post/<int:pk>/delete/", views.DeletePostView.as_view(), name="delete"),
	path("posts/<int:pk>/", views.DetailsPostView.as_view(), name="details"),
	path("delete/success/", views.delete_success, name="delete-success"),
]