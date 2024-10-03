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

    def borrow_book(self, user: User, book_id: int) -> None:
        self.borrowed_books[user.user_id].append(book_id)

    def return_book(self, book_id: int) -> None:
        for key in self.borrowed_books.keys():
            books = self.borrowed_books.get(key)
            if book_id in books:
                books.remove(book_id)
                return

    def add_book(self, book: Book):
        self.books[book.title].append(book)


user1 = User(0, "Jan", "Kowalski", "123456789")
user2 = User(1, "John", "Matador", "987654321")

library = Library()
