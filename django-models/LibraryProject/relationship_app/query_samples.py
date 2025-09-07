from .models import Author, Book, Library, Librarian
author_name = "John Green"
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)

library_name = "New Library"
library = Library.objects.get(name=library_name)
library.books.all()

new_library = Library.objects.get(name=library_name)
Librarian.objects.filter(library=new_library).values()