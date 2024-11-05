class HomeLibrary:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, book_info):
        self.books[book_id] = book_info

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            print("Book not found")

    def search_by_author(self, author):
        return [book for book in self.books.values() if book['author'] == author]

    def search_by_year(self, year):
        return [book for book in self.books.values() if book['year'] == year]

 

    def search_by_genre(self, genre):
        return [book for book in self.books.values() if book['genre'] == genre]

    def get_book(self, book_id):
        return self.books.get(book_id, "Book not found")

    def list_books(self):
        for book_id, book_info in self.books.items():
            print(f"ID: {book_id}, Info: {book_info}")

 

