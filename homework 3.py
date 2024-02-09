class Book:
   def __init__(self, title, author, year):
       self.title = title
       self.author = author
       self.year = year
       self.status = "available"


class Library:
   def __init__(self):
       self.books = []
   def add_book(self, book):

       self.books.append(book)
   def remove_book(self, book):
       self.books.remove(book)


   def lend_book(self, book):
       if book.status == "available":
           book.status = "lent"
           print(f"{book.title} by {book.author} has been lent out.")
       else:
           print("Sorry, this book is not available.")


   def return_book(self, book):
       if book.status == "lent":
           book.status = "available"
           print(f"{book.title} by {book.author} has been returned.")
       else:
           print("This book was not lent out.")




library = Library()
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("1984", "George Orwell", 1949)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.lend_book(book1)

library.return_book(book1)