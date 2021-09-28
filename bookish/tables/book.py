class Book:
    def __init__(self, title, author, coverPhotoUrl, bookId=None):
        self.bookId = bookId
        self.title = title
        self.author = author
        self.coverPhotoUrl = coverPhotoUrl

    def __str__(self) -> str:
        return f'BookId: {self.bookId}, Title: {self.title}, Author: {self.author}, CoverPhotoUrl: {self.coverPhotoUrl}'
