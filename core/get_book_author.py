import os
from core import BookNotFoundError


def get_book_author(book_name):
    if not os.path.isdir(os.path.join("Книги", book_name)):
        raise BookNotFoundError(book_name)
    try:
        with open(os.path.join("Книги", book_name, 'Автор.txt'), 'r', encoding='utf-8') as file:
            f=file.read().rstrip('\n')
            return f
    except FileNotFoundError:
        return 'Неизвестный автор'

