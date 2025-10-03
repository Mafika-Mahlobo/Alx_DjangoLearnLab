from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class CustomForm(UserCreationForm):
	email = forms.EmailField()
	username = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)

	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email"]


class CustomUserUpdateForm(UserChangeForm):
	email = forms.EmailField()
	username = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)

	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email"]