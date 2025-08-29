## delete
command1: from bookshelf.models import Book
command2: book.delete()
output2: (1, {'bookshelf.Book': 1})
command2: Book.objects.get(id=new_book.id)
output2: <QuerySet []>
