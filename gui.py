from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

books = [
    # this should be removed later on oke ? 
    # TODO make it fetch automatic
    {"title": "book1", "author": "nn", "cover": "covers/cover1.png"},
    {"title": "book2", "author": "nn", "cover": "covers/cover2.png"},
    {"title": "book3", "author": "nn", "cover": "covers/cover3.png"},
    {"title": "test", "author": "def not me", "cover": "covers/cover4.png"},
    {"title": "testtesttest", "author": "def not me", "cover": "covers/cover5.png"},
    {"title": "ebook1", "author": "me >:D", "cover": "covers/cover6.png"},
    {"title": "ebook2", "author": "me >:D", "cover": "covers/cover7png"},
    {"title": "ebook3", "author": "me >:D", "cover": "covers/cover8.png"},
    {"title": "book6", "author": "nn", "cover": "covers/cover1.png"},
    {"title": "book7", "author": "nn", "cover": "covers/cover2.png"},
    {"title": "book8", "author": "nn", "cover": "covers/cover3.png"},
    {"title": "book9", "author": "nn", "cover": "covers/cover1.png"},
    {"title": "book0", "author": "nn", "cover": "covers/cover2.png"},
    {"title": "book124", "author": "nn", "cover": "covers/cover3.png"},
    {"title": "book43", "author": "nn", "cover": "covers/cover1.png"},
    {"title": "book543", "author": "nn", "cover": "covers/cover2.png"},
    {"title": "book55", "author": "nn", "cover": "covers/cover3.png"},
]

class BookGrid(GridLayout):
    def __init__(self, **kwargs):
        super(BookGrid, self).__init__(**kwargs)
        self.cols = 3
        self.spacing = 10
        self.padding = 10
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        self.populate_grid(books)

    def populate_grid(self, books_to_display):
        self.clear_widgets()
        for book in books_to_display:
            book_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=250)
            
            cover_image = Image(source=book["cover"], size_hint_y=None, height=200)
            book_layout.add_widget(cover_image)
            
            title_label = Label(text=book["title"], size_hint_y=None, height=30)
            author_label = Label(text=book["author"], size_hint_y=None, height=20)
            book_layout.add_widget(title_label)
            book_layout.add_widget(author_label)
            
            self.add_widget(book_layout)

class EBookReaderApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        self.search_input = TextInput(hint_text="Search by title or author", size_hint_y=None, height=50)
        self.search_input.bind(text=self.on_search)
        main_layout.add_widget(self.search_input)
        
        scroll_view = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        
        self.book_grid = BookGrid()
        scroll_view.add_widget(self.book_grid)
        
        main_layout.add_widget(scroll_view)
        
        return main_layout

    def on_search(self, instance, value):
        query = value.lower()
        filtered_books = [
            book for book in books
            if query in book["title"].lower() or query in book["author"].lower()
        ]
        self.book_grid.populate_grid(filtered_books)

if __name__ == '__main__':
    EBookReaderApp().run()