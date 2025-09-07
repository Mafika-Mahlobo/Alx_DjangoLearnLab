## update
command1: new_book.title = "Nineteen Eighty-Four"
output1: No output
command2: new_book.save()
output2: No output
command3: Book.objects.all().values() 
output3: <QuerySet [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]>