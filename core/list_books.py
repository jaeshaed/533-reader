import os


def list_books(search = None):
    spisok = []
    for filename in os.listdir("Книги"):
        filename_with_path = os.path.join("Книги", filename)
        if os.path.isdir(filename_with_path):
            if search is None:
                spisok.append(filename_with_path)
            elif search in filename_with_path:
                spisok.append(filename_with_path)
    return spisok