def add_book(book_name, book_text):
    with open(f"Книги/{book_name}.txt", "w") as book_file:
        book_file.write(book_text)
