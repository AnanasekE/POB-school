class BookAlreadyInLibraryException(Exception):
    pass


class UserAlreadyRegisteredException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, genre: str):
        self.book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.genre: str = genre


class User:
    def __init__(self, user_id: int, name: str, surname: str, phone: str):
        self.user_id: int = user_id
        self.name: str = name
        self.surname: str = surname
        self.phone: str = phone


class Library:
    def __init__(self):
        self.books: dict[str, list[Book]] = {}
        self.borrowed_books: dict[int, list[int]] = {}
        self.users: list[User] = []

    def borrow_book(self, user: User, book_id: int) -> None:
        if self.borrowed_books.get(user.user_id) is None:
            self.borrowed_books[user.user_id] = []
        for key in self.borrowed_books.keys():
            if book_id in self.borrowed_books.get(key):
                raise BookAlreadyBorrowedException()

        self.borrowed_books.get(user.user_id).append(book_id)

    def return_book(self, book_id: int) -> None:
        for key in self.borrowed_books.keys():
            books = self.borrowed_books.get(key)
            if book_id in books:
                books.remove(book_id)
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
            print(key)


user1 = User(0, "Jan", "Kowalski", "123456789")
user2 = User(1, "John", "Matador", "987654321")

book1 = Book(0, "Title1", "Jan Kowalski", 2024, "Horror")
book2 = Book(1, "Title1", "Jan Kowalski", 2024, "Horror")
book3 = Book(2, "Title2", "Marek Kobyla", 2023, "Children Stories")

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
library.borrow_book(user1, book2.book_id)
assert book2.book_id in library.borrowed_books[user1.user_id]

try:
    library.borrow_book(user2, book2.book_id)
except BookAlreadyBorrowedException:
    print("Book already borrowed")

print("Printing all titles")
library.print_books()

library.return_book(book2.book_id)
assert book2.book_id not in library.borrowed_books.get(user2.user_id)
