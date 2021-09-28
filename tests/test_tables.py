from bookish.tables.book import Book
from bookish.tables.book_copy import BookCopy
from bookish.tables.loan import Loan
from bookish.tables.member import Member

def test_book():
    book = Book('Moby Dick', 'Bob Smith', 'http://url.com', 1)
    assert str(book) == 'BookId: 1, Title: Moby Dick, Author: Bob Smith, CoverPhotoUrl: http://url.com'
    book = Book('Moby Dick', 'Bob Smith', 'http://url.com')
    assert str(book) == 'BookId: None, Title: Moby Dick, Author: Bob Smith, CoverPhotoUrl: http://url.com'

def test_book_copy():
    bookCopy = BookCopy(1, 2)
    assert str(bookCopy) == 'BookId: 1, BookCopyId: 2'

def test_loan():
    loan = Loan(1, 2, 3, '1/1/1970')
    assert str(loan) == 'BookId: 1, BookCopyId: 2, MemberId: 3, DueDate: 1/1/1970'

def test_member():
    member = Member('Bob', 'Smith', 1)
    assert str(member) == 'MemberId: 1, FirstName: Bob, LastName: Smith'
    member = Member('Bob', 'Smith', None)
    assert str(member) == 'MemberId: None, FirstName: Bob, LastName: Smith'