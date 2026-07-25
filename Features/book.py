# This file manages individual books

class Book():
    def __init__(self, name, author, description = ""):
        self.name = name
        self.author = author
        self.description = description
        self.rating = None
        self.is_read = False
    
    def rate(self, rating):
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5.")
        self.rating = rating

    def mark_as_read(self):
        self.is_read = True


class BookVault():
    def __init__(self):
        self.books = []

    def add_book(self):
        choice = input('Do you want to add a book ? (y/n): ')
        if not choice in ('y', 'n'):
            raise ValueError('Please choice between (y/n).')
        elif choice == 'y':
            Book(self.name, self.author, self.description)
        elif choice == 'n':
            print('Returning to main menu...')
        self.books.append(self.book)
    
    def remove_book(self):
        pass
    
    def view_books(self):
        pass
    
    def search_books(self):
        pass