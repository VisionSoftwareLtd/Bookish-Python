import logging
import sqlite3
from sqlite3 import Error

from bookish.tables.book import Book
from bookish.tables.book_copy import BookCopy
from bookish.tables.loan import Loan
from bookish.tables.member import Member


class Database:
    def __init__(self, databasePath):
        self.__conn = None
        try:
            self.__conn = sqlite3.connect(databasePath)
        except Error as e:
            logging.error(e)
            raise e

    def __del__(self):
        if self.__conn is not None:
            self.__conn.close()

    def getBooks(self) -> []:
        books = []
        sql = 'SELECT * FROM Book'
        cursor = self.__conn.cursor()
        cursor.execute(sql)
        booksData = cursor.fetchall()
        cursor.close()
        for book in booksData:
            books.append(Book(book[0], book[1], book[2], book[3]))
        return books

    def getBookByTitle(self, title) -> Book or None:
        sql = 'SELECT * FROM Book WHERE Title=?'
        titleData = (title, )
        cursor = self.__conn.cursor()
        cursor.execute(sql, titleData)
        book = cursor.fetchone()
        if book is not None:
            return Book(book[1], book[2], book[3], book[0])
        return None

    def addBook(self, book) -> Book:
        sql = 'INSERT INTO Book (Title, Author, CoverPhotoUrl) VALUES (?, ?, ?)'
        cursor = self.__conn.cursor()
        bookData = (book.title, book.author, book.coverPhotoUrl)
        cursor.execute(sql, bookData)
        book.bookId = cursor.lastrowid
        cursor.close()
        self.__conn.commit()
        return book

    def updateBook(self, book):
        sql = 'UPDATE Book SET Title=?, Author=?, CoverPhotoUrl=? WHERE BookId=?'
        cursor = self.__conn.cursor()
        bookData = (book.title, book.author, book.coverPhotoUrl, book.bookId)
        cursor.execute(sql, bookData)
        cursor.close()
        self.__conn.commit()

    def deleteBook(self, book):
        sql = 'DELETE FROM Book WHERE BookID=?'
        cursor = self.__conn.cursor()
        bookData = (book.bookId, )
        cursor.execute(sql, bookData)
        cursor.close()
        self.__conn.commit()

    def deleteBookCopy(self, bookCopy):
        sql = 'DELETE FROM BookCopy WHERE BookID=? AND BookCopyID=?'
        cursor = self.__conn.cursor()
        bookData = (bookCopy.bookId, bookCopy.bookCopyId)
        cursor.execute(sql, bookData)
        cursor.close()
        self.__conn.commit()

    def deleteMember(self, member):
        sql = 'DELETE FROM Member WHERE MemberID=?'
        cursor = self.__conn.cursor()
        bookData = (member.memberId, )
        cursor.execute(sql, bookData)
        cursor.close()
        self.__conn.commit()

    def deleteLoan(self, loan):
        sql = 'DELETE FROM Loan WHERE BookID=? AND BookCopyID=? AND MemberID=?'
        cursor = self.__conn.cursor()
        bookData = (loan.bookId, loan.bookCopyId, loan.memberId)
        cursor.execute(sql, bookData)
        cursor.close()
        self.__conn.commit()

    def addMember(self, member) -> Member:
        sql = 'INSERT INTO Member (FirstName, LastName) VALUES (?, ?)'
        cursor = self.__conn.cursor()
        memberData = (member.firstName, member.lastName)
        cursor.execute(sql, memberData)
        member.memberId = cursor.lastrowid
        cursor.close()
        self.__conn.commit()
        return member

    def getBookCopiesForBook(self, book) -> []:
        bookCopies = []
        sql = 'SELECT * FROM BookCopy WHERE BookId=?'
        bookCopyData = (book.bookId, )
        cursor = self.__conn.cursor()
        cursor.execute(sql, bookCopyData)
        bookCopyData = cursor.fetchall()
        cursor.close()
        for bookCopy in bookCopyData:
            bookCopies.append(BookCopy(bookCopy[0], bookCopy[1]))
        return bookCopies

    def addBookCopy(self, book) -> BookCopy:
        bookCopies = self.getBookCopiesForBook(book)
        maxBookCopyId = 0
        for bookCopy in bookCopies:
            if bookCopy.bookCopyId > maxBookCopyId:
                maxBookCopyId = bookCopy.bookCopyId
        newBookCopy = BookCopy(book.bookId, maxBookCopyId + 1)
        sql = 'INSERT INTO BookCopy (BookID, BookCopyID) VALUES (?, ?)'
        cursor = self.__conn.cursor()
        memberData = (newBookCopy.bookId, newBookCopy.bookCopyId)
        cursor.execute(sql, memberData)
        cursor.close()
        self.__conn.commit()
        return newBookCopy

    def getLoansForBook(self, book) -> []:
        loans = []
        sql = 'SELECT * FROM Loan WHERE BookId=?'
        loanData = (book.bookId, )
        cursor = self.__conn.cursor()
        cursor.execute(sql, loanData)
        loanData = cursor.fetchall()
        cursor.close()
        for loan in loanData:
            loans.append(Loan(loan[0], loan[1], loan[2], loan[3]))
        return loans

    def __getBooksNotOnLoan(self, bookCopies, loans) -> []:
        availableBookCopies = []
        for bookCopy in bookCopies:
            inUse = False
            for loan in loans:
                if loan.bookId == bookCopy.bookId and loan.bookCopyId == bookCopy.bookCopyId:
                    inUse = True
                    break
            if not inUse:
                availableBookCopies.append(bookCopy)
        return availableBookCopies

    def checkoutBook(self, book, member) -> Loan or None:
        bookCopies = self.getBookCopiesForBook(book)
        loans = self.getLoansForBook(book)
        booksAvailable = self.__getBooksNotOnLoan(bookCopies, loans)
        if len(booksAvailable) == 0:
            return None
        loan = Loan(book.bookId, booksAvailable[0].bookCopyId, member.memberId, '1/1/1970')
        sql = 'INSERT INTO Loan (BookID, BookCopyID, MemberID, DueDate) VALUES (?, ?, ?, ?)'
        cursor = self.__conn.cursor()
        loanData = (loan.bookId, loan.bookCopyId, loan.memberId, loan.dueDate)
        cursor.execute(sql, loanData)
        cursor.close()
        self.__conn.commit()
        return loan

    def getBooksTakenOutByMember(self, member) -> []:
        return []
