class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# Misol:
library = Library()
book1 = Book("Kitob 1", "Muallif 1")
book2 = Book("Kitob 2", "Muallif 2")

library.add_book(book1)
library.add_book(book2)

print(library.search_book("Kitob 1").title)  # Kitob 1
library.remove_book("Kitob 1")
print(library.search_book("Kitob 1"))  # None
