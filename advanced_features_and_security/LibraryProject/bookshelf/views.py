from django.shortcuts import render, redirect, HttpResponse



def book_list_view(request):
	if request.user.has_perm("bookshelf.can_view"):
		return HttpResponse("You are allowed ro view books!")
	return HttpResponse("Access denied!")



def book_add_view(request):
	if request.user.has_perm("bookshelf.can_create"):
		return HttpResponse("You can go ahead and add a book")
	return HttpResponse("Access denied!")


def book_edit_view(request):
	if request.user.has_perm("bookshelf.can_edit"):
		return HttpResponse("You can go ahead and edit books")
	return HttpResponse("Access denied!")

def book_delete_view(request):
	if request.user.has_perm("bookshelf.can_delete"):
		return HttpResponse("You can delete a book")
	return HttpResponse("Access denied!")
