from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomForm, CustomUserUpdateForm
from django.contrib.auth.decorators import login_required

def register_view(request):
	if request.method == "POST":
		form = CustomForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
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