from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomForm, CustomUserUpdateForm
from django.contrib.auth.decorators import login_required

def register_view(request):
	if request.method == "POST":
		form = CustomForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("home")
	else:
		form = CustomForm()

	return render(request, "blog/register.html", {"form": form})


@login_required
def home_view(request):
	if request.method == "POST":
		form = CustomUserUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = CustomUserUpdateForm(instance=request.user)

	return render(request, "blog/profile.html", {"form": form})


class ListPostsView(LoginRequiredMixin, generic.ListView):
	model = Post
	context_object_name = "post"
	template_name = "blog/posts.html"
	login_url = "login"
	
class CreatePostView(LoginRequiredMixin, generic.CreateView):
	model = Post
	template_name = "blog/create_post.html"
	fields = ["title", "content"]
	success_url = reverse_lazy("posts")

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class EditPostView(LoginRequiredMixin, UserPassesTestMixin ,generic.UpdateView):
	model = Post
	fields = ["title", "content"]
	template_name = "blog/edit_post.html"
	success_url = reverse_lazy("posts")

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
	model = Post
	success_url = reverse_lazy("posts")

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class DetailsPostView(LoginRequiredMixin, generic.DetailView):
	model = Post
	template_name = "blog/detail.html"
	login_url = "login"
	context_object_name = "post"