#create class book
class Book:
    #initialize all the parameters
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
       
#checks whether the book is available or not
    def available(self,available_book):
        if available_book:
         print("book avaialable")
        else:
         print("book not available")
#displays all info inputed by book borrower about the book
    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
#prompts user to input book info
title=input("input book title\n")  
author=input("input author name\n")
publication_year=int(input("enter publication year\n"))  
available_book=input("enter whether book has been returned or not(true/false):")
#book availability
available_book=available_book.lower()=='true'
 # Create book objects
book = Book(title, author, publication_year)
# Display book information
book.display_info()
#book availability
book.available(available_book)