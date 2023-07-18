#create a class called book
class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books =[] 
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
#display member info
    def display_info(self):
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("number of borrowed books:",len(self.borrowed_books))
#input member info        
member_id=input("input member id\n")
name=input("input member name\n")
#create a new instance of the Book class for each book borrowed
num_book=int(input("input number of books borrowed\n"))
# Create library member object
member = LibraryMember(member_id, name)
class Book(LibraryMember):
    def __init__(self, title, author, publication_year,member_id, name):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.member_id = member_id
        self.name = name
    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
title=input("input book title\n")
author=input("input book author\n")
publication_year=int(input("enter publication year\n"))
book_object = Book(title, author, publication_year,member_id,name)
#create a class called LibraryMember

# Borrow books
for _ in range(num_book):
    member.borrow_book(Book(title, author, publication_year,member_id,name))
# Display member information
book_object.display_info()
# Return a book
member.return_book(book_object)

# Display updated member information
member.display_info()