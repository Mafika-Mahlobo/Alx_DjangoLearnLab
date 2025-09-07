from .models import Author, Book, Library, Librarian

john = Author.objects.get(name="John Green")
Book.objects.filter(author=john).values()

library_name = "New Library"
books = Library.objects.get(name=library_name)
books.objects.all()

new_library = Library.objects.get(name=library_name)
Librarian.objects.filter(library=new_library).values()