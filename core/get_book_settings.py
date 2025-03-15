import os


def get_book_settings(book_name):
    with open(os.path.join("Книги", book_name, 'Настройки.json'), 'r', encoding='utf-8') as file:
        f = file.read().rstrip('\n')
        print(f)