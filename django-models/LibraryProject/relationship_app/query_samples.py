from .models import Author, Book, Library, Librarian

john = Author.objects.get(name="John Green")
Book.objects.filter(author=john).values()

library_name = "New Library"
library = Library.objects.get(name=library_name)
library.books.all()

new_library = Library.objects.get(name=library_name)
Librarian.objects.filter(library=new_library).values()