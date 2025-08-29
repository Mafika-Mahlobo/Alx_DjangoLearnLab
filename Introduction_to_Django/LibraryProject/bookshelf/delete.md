## delete
command1: new_book.delete()
output1: (1, {'bookshelf.Book': 1})
command2: Book.objects.all().values()
output2: <QuerySet []>