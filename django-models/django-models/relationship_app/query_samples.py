from .models import Author, Book, Library, Librarian

john = Author.objects.get(name="John Green")
Book.objects.filter(author=john).values()

Book.objects.all().values()

new_library = Library.objects.get(name="New Library")
Librarian.objects.filter(library=new_library).values()