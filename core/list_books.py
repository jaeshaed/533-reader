import os


directory = "Книги"
name = input("введите книгу: ")
def list_books(filter = None):
    for filename in os.listdir("Книги"):
        filename_with_path = os.path.join("Книги", filename)
        if os.path.isdir(filename_with_path):
            if name in filename_with_path:
                print(filename_with_path)