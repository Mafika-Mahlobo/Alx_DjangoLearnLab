#Django ORM CRUD Operations

##create
command1: new_book = Book(title="1984", author="George Orwell", publication_year=1949)
Output1: No output
command2: new_book.save()
output2: No output

##retrieve
command: Book.objects.all().values()
output: <QuerySet [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>

##update
command1: new_book.title = "Nineteen Eighty-Four"
output1: No output
command2: new_book.save()
output2: No output
command3: Book.objects.all().values() 
output3: <QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>

##delete
command1: new_book.delete()
output1: (1, {'bookshelf.Book': 1})
command2: Book.objects.all().values()
output2: <QuerySet []>
