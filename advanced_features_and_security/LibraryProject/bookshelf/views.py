from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import permission_required



@permission_required("bookshelf.can_view", raise_exception=True)
def book_list_view(request):
	return HttpResponse("You are allowed ro view books!")
	

@permission_required("bookshelf.can_create", raise_exception=True)
def book_add_view(request):
	return HttpResponse("You can go ahead and add a book")
	

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit_view(request):
	return HttpResponse("You can go ahead and edit books")


@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete_view(request):
	return HttpResponse("You can delete a book")
	
