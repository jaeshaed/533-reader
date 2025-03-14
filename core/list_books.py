"""List_books. Возвращает список книг."""

import os


def list_books(search = None):
    """Функция list_books(), с пустыми скобками возвращает полный список книг"""
    spisok = []
    for filename in os.listdir("Книги"):
        filename_with_path = os.path.join("Книги", filename)
        if os.path.isdir(filename_with_path):
            if search is None:
                spisok.append(filename_with_path)
            elif search.lower() in filename_with_path.lower():
                spisok.append(filename_with_path)
    return spisok
