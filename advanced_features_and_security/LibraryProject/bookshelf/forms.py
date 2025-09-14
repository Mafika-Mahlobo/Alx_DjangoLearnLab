from django import forms

class ExampleForm(forms.Form):
	username = forms.CharField(max_length=100)
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
	password = forms.CharField(widget=forms.PasswordInput())
