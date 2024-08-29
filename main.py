import json
import unittest

class Book:
    def __init__(self, title: str, author: str, weight: float, cost:
    float):
        self.title = title
        self.author = author
        self.weight = weight
        self.cost = cost


class Bookshelf:
    def __init__(self, max_weight: float):
        self.max_weight = max_weight
        self.books = []


def add_book(self, book: Book) -> None:
    if self.current_weight() + book.weight <= self.max_weight:
        self.books.append(book)
    else:
        print("Cannot add book, shelf is full")


def remove_book(self, title: str) -> None:
    for book in self.books:
        if book.title == title:
            self.books.remove(book)
            return print("Book not found")


def search_by_author(self, author: str) -> list:
    return [book for book in self.books if book.author == author]


def total_weight(self) -> float:
    return sum(book.weight for book in self.books)


def total_cost(self) -> float:
    return sum(book.cost for book in self.books)


def current_weight(self) -> float:
    return sum(book.weight for book in self.books)


def to_json(self, filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump({'max_weight': self.max_weight,
                   'books': [(book.title, book.author, book.weight, book.cost) for book in self.books]}, f)


@classmethod
def from_json(cls, filename: str):
    with open(filename, 'r') as f:
        data = json.load(f)
        bookshelf = cls(data['max_weight'])
        for book_data in data['books']:
            bookshelf.add_book(Book(*book_data))
            return bookshelf


def to_txt(self, filename: str) -> None:
    with open(filename, 'w') as f:
        f.write(f"Max Weight: {self.max_weight}\n")
        for book in self.books:
            f.write(f"Title: 	{book.title}, 	Author: {book.author}, Weight: {book.weight}, Cost: {book.cost}\n")


@classmethod
def from_txt(cls, filename: str):
    with open(filename, 'r') as f:
        lines = f.readlines()
        max_weight = float(lines[0].split(": ")[1])
        bookshelf = cls(max_weight)
        for line in lines[1:]:
            title, author, weight, cost = line.strip().split(", ")
            bookshelf.add_book(Book(title.split(": 	")[1], author.split(": ")[1], float(weight.split(": ")[1]), float(cost.split(":")[1])))
            return bookshelf 


class TestBookshelf(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Title1", "Author1", 1.5, 20.0)
        self.book2 = Book("Title2", "Author2", 1.0, 15.0)
        self.book3 = Book("Title3", "Author1", 2.0, 25.0)
        self.bookshelf = Bookshelf(5.0)


def test_add_book(self):
    self.bookshelf.add_book(self.book1)
    self.assertIn(self.book1, self.bookshelf.books)


def test_remove_book(self):
    self.bookshelf.add_book(self.book1)
    self.bookshelf.remove_book("Title1")
    self.assertNotIn(self.book1, self.bookshelf.books)


def test_search_by_author(self):
    self.bookshelf.add_book(self.book1)
    self.bookshelf.add_book(self.book2)
    self.bookshelf.add_book(self.book3)
    self.assertEqual(len(self.bookshelf.search_by_author("Author1")), 2)


def test_total_cost(self):
    self.bookshelf.add_book(self.book1)
    self.bookshelf.add_book(self.book2)
    self.bookshelf.add_book(self.book3)
    self.assertEqual(self.bookshelf.total_cost(), 60.0)


if __name__ == '__main__':
    unittest.main()
