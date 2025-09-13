from .models import Author, Book, Library, Librarian
author_name = "John Green"
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)

library_name = "New Library"
library = Library.objects.get(name=library_name)
library.books.all()

librarian = Librarian.objects.get(library=library_name)
librarian.objects.all()