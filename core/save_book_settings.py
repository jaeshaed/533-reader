"""сохранение настроек в Настройки.json"""

import json


def save_settings(book_name, settings):
    """это функция сохранения настроек в файл-JSON
        book_name = название книги
        settings = словарь с настройками книги """
    filename = f"Книги/{book_name}/Настройки.json"
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(settings,file, ensure_ascii=False, indent=4)
