import os
import shutil

def delete_book(book_name):
    shutil.rmtree(os.path.join("Книги", book_name))
