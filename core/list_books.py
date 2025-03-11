import os


directory = "Книги"
spisok = []
def list_books(filter = None):
    for filename in os.listdir("Книги"):
        filename_with_path = os.path.join("Книги", filename)
        if os.path.isdir(filename_with_path):
            if filter in filename_with_path:
                spisok.append(filename_with_path)