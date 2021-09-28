class BookCopy:
    def __init__(self, bookId, bookCopyId):
        self.bookId = bookId
        self.bookCopyId = bookCopyId

    def __str__(self) -> str:
        return f'BookId: {self.bookId}, BookCopyId: {self.bookCopyId}'
