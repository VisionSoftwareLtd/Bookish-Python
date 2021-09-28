import logging

from bookish import DATABASE_PATH, LOGFILE_PATH
from bookish.database import Database
from bookish.tables.book import Book
from bookish.tables.member import Member

logging.basicConfig(filename=LOGFILE_PATH)

database = Database(DATABASE_PATH)
book = Book('TestTitle', 'TestAuthor', 'TestUrl')
book = database.addBook(book)
bookCopy = database.addBookCopy(book)
member = Member('Bob', 'Smith')
member = database.addMember(member)
loan = database.checkoutBook(book, member)
print(loan)

# try:
#     conn = sqlite3.connect(DATABASE_PATH)
# except Error as e:
#     print(e)
#
# # Create a cursor to allow to execute SQL commands
# cursor = conn.cursor()
#
# # Create a SQL Table
# sql_command = '''
#     CREATE TABLE IF NOT EXISTS contacts (
#         Id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Firstname TEXT,
#         Lastname TEXT,
#         Email TEXT
#     )'''
#
# cursor.execute(sql_command)
#
# firstName = '; DROP TABLE Member;'
# lastName = 'Smith'
#
# selectStatement = f'SELECT * FROM Member WHERE FirstName={firstName} AND LastName={lastName}'
#
# # Commit the changes to the database
# conn.commit()
#
# # insert_data = """
# #     INSERT INTO contacts
# #     (Firstname, Lastname, Email)
# #     VALUES (
# #         'David',
# #         'Attenborough',
# #         'dattenborough@example.com'
# #     )
# # """
# # cursor.execute(insert_data)
# #
# # # Commit the changes to the database
# # conn.commit()
#
# # select_data = 'SELECT * FROM contacts'
# # cursor.execute(select_data)
# #
# # row = cursor.fetchone()
# #
# # print(row)
#
# select_data = 'SELECT * FROM contacts'
#
# df = pd.read_sql_query(select_data, conn)
# print(df)
#
# conn.close()