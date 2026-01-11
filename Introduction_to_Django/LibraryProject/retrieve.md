books = Book.objects.all()
books
book = books.first()
book.title, book.author, book.publication_year
