#create a class called book
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)

title=input("input book title\n")
author=input("input book author\n")
publication_year=int(input("enter publication year\n"))

book_object = Book(title, author, publication_year)

 #create a class called LibraryMember

class LibraryMember(Book):
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
        print("number of borrowed books:")
#input member info        
member_id=input("input member id\n")
name=input("input member name\n")
book=int(input("input number of books borrowed\n"))

# Create library member object
member = LibraryMember(member_id, name)
# Borrow books
for _ in range(book):
    member.borrow_book(book_object)

member.borrow_book(book)


# Display member information
member.display_info()

# Return a book
member.return_book(book_object)
for _ in range(book):
    member.return_book(book_object)
# Display updated member information
book_object.display_info()