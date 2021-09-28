import os

from bookish import DATABASE_PATH
from bookish.database import Database
from bookish.tables.book import Book
from bookish.tables.member import Member

if os.getcwd().endswith('tests'):
    databasePath = f'../bookish/{DATABASE_PATH}'
else:
    databasePath = f'bookish/{DATABASE_PATH}'

def test_normal_sequence():
    database = Database(databasePath)

    book = Book('TestTitle', 'TestAuthor', 'TestUrl')
    book = database.addBook(book)
    assert book.bookId is not None

    bookCopy = database.addBookCopy(book)
    assert bookCopy.bookCopyId is not None

    member = Member('TestFirstName', 'TestLastName')
    member = database.addMember(member)
    assert member.memberId is not None

    loan = database.checkoutBook(book, member)
    assert loan.bookCopyId == bookCopy.bookCopyId

    database.deleteBook(book)
    database.deleteBookCopy(bookCopy)
    database.deleteMember(member)
    database.deleteLoan(loan)

def test_book_modifications():
    database = Database(databasePath)

    book = Book('TestTitle', 'TestAuthor', 'TestUrl')
    book = database.addBook(book)
    assert book.bookId is not None
    bookId = book.bookId

    book = database.getBookByTitle('TestTitle')
    assert book.bookId == bookId

    database.deleteBook(book)
    book = database.getBookByTitle('TestTitle')
    assert book is None