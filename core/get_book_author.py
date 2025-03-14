import os


def get_book_author(book_name):
    try:
        with open(os.path.join("Книги", book_name, 'Автор.txt'), 'r', encoding='utf-8') as file:
            f=file.read().rstrip('\n')
            return f
    except FileNotFoundError:
        return 'Неизвестный автор'

