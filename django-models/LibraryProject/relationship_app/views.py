from django.shortcuts import render
from  .models import Book, Author
from .models import Library
from django.views.generic import DetailView

def list_books(request):

    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library" 

    def get_object(self):

        author, _ = Author.objects.get_or_create(name="J R.R Martin")
        book, _ = Book.objects.get_or_create(title="A Song of Ice and Fire", author=author, publication_year=1996)
        library, _ = Library.objects.get_or_create(name="New Library")
        
        if not library.books.filter(pk=book.pk).exists():
            library.books.add(book)

        return library

    