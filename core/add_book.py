import os


def add_book(book_name, book_text):
    os.mkdir(f"Книги/{book_name}")
    with open(f"Книги/{book_name}/Текст.txt", "w") as book_file:
        book_file.write(book_text)
