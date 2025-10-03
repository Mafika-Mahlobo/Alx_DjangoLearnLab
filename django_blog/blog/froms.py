from django import forms

class CustomForm(forms.Form):
	email = forms.EmailField()