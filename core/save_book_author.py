import os

def save_book_author(book_name, author):
    filename = os.path.join('Книги', book_name, 'Автор.txt')
    with open(filename,'w')as file:
       file.write(author)



