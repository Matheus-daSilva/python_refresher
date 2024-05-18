from typing import List

# ------------------------------------

class Book:
    pass

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:    
        return "BookShelf..."