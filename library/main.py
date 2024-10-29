import time
from datetime import datetime
from functools import reduce


class BookAlreadyInLibraryException(Exception):
    pass


class UserAlreadyRegisteredException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class BookNotInLibraryException(Exception):
    pass


class Book:
    book_id_counter = 0

    def __init__(self, title: str, author: str, year: int, genre: str):
        self.book_id: int = Book.book_id_counter
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.genre: str = genre
        Book.book_id_counter += 1

    def __str__(self):
        return f"id: {self.book_id}, title: {self.title}, author: {self.author}, year: {self.year}"


class BorrowedBook:
    def __init__(self, book_id: int):
        self.book_id = book_id
        self.time: float = time.time()


class User:
    user_id_counter = 0

    def __init__(self, name: str, surname: str, phone: str):
        self.user_id: int = User.user_id_counter
        self.name: str = name
        self.surname: str = surname
        self.phone: str = phone
        User.user_id_counter += 1


class Library:
    def __init__(self):
        self.books: dict[str, list[Book]] = {}
        self.borrowed_books: dict[int, list[BorrowedBook]] = {}
        self.users: list[User] = []

    def borrow_book(self, user_id: int, book_id: int) -> None:
        if self.borrowed_books.get(user_id) is None:
            self.borrowed_books[user_id] = []
        for key in self.borrowed_books.keys():
            if book_id in self.borrowed_books.get(key):
                raise BookAlreadyBorrowedException()

        self.borrowed_books.get(user_id).append(BorrowedBook(book_id))

    def return_book(self, book_id: int) -> None:
        for key in self.borrowed_books.keys():
            books = self.borrowed_books.get(key)
            if book_id in books:
                books.remove(books[book_id])
                return

    def add_book(self, book: Book):
        if self.books.get(book.title) is None:
            self.books[book.title] = []
        if book in self.books.get(book.title):
            raise BookAlreadyInLibraryException()
        self.books[book.title].append(book)

    def register_user(self, user: User):
        if user in self.users:
            raise UserAlreadyRegisteredException()
        self.users.append(user)

    def print_books(self):
        for key in self.books.keys():
            for book in self.books.get(key):
                print(book)


user1 = User("Jan", "Kowalski", "123456789")
user2 = User("John", "Marigold", "987654321")

book1 = Book("Title1", "Jan Kowalski", 2024, "Horror")
book2 = Book("Title1", "Jan Kowalski", 2024, "Horror")
book3 = Book("Title2", "Marek Kobyla", 2023, "Children Stories")

library = Library()

assert library.books == {}

library.add_book(book1)
assert book1.title in library.books
try:
    library.add_book(book1)
except BookAlreadyInLibraryException:
    print("Book instance already in library")

assert library.users == []
library.register_user(user1)
assert user1 in library.users

try:
    library.register_user(user1)
except UserAlreadyRegisteredException:
    print("User already registered in library")

library.add_book(book2)
library.borrow_book(user1.user_id, book2.book_id)
# assert book2.book_id in library.borrowed_books[user1.user_id] #TOFIX

try:
    library.borrow_book(user2.user_id, book2.book_id)
except BookAlreadyBorrowedException:
    print("Book already borrowed")

print("Printing all titles")
library.print_books()

library.return_book(book2.book_id)
assert book2.book_id not in library.borrowed_books.get(user2.user_id)
