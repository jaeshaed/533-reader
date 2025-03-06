from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

books = [
    {"title": "book1", "author": "nn", "cover": "covers/cover1.png"},
    {"title": "book2", "author": "nn", "cover": "covers/cover2.png"},
    {"title": "book3", "author": "nn", "cover": "covers/cover3.png"},
]

class BookGrid(GridLayout):
    def __init__(self, **kwargs):
        super(BookGrid, self).__init__(**kwargs)
        self.cols = 2
        self.spacing = 10
        self.padding = 10
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        self.populate_grid()

    def populate_grid(self):
        for book in books:
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
        scroll_view = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        
        book_grid = BookGrid()
        scroll_view.add_widget(book_grid)
        
        return scroll_view

if __name__ == '__main__':
    EBookReaderApp().run()