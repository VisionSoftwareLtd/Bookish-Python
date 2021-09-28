class Loan:
    def __init__(self, bookId, bookCopyId, memberId, dueDate):
        self.bookId = bookId
        self.bookCopyId = bookCopyId
        self.memberId = memberId
        self.dueDate = dueDate

    def __str__(self) -> str:
        return f'BookId: {self.bookId}, BookCopyId: {self.bookCopyId}, MemberId: {self.memberId}, DueDate: {self.dueDate}'
