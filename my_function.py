from book import Book
import json

#print options
def print_options():
    print("Press the specific button for that action")
    print(" 1- create a new book")
    print("2- save books locally")
    print("3- load books from the disk ")
    print("4- issue book")
    print("5- return a book")
    print("6- update a book")
    print("7- show all books ")
    print("8-show book")

#input book info function
def input_book_info():
    id = input("ID:")
    name = input("Name: ")
    description = input("Description:")
    isbn = input("ISBN: ")
    page_count = int(input("Page count: "))
    issued = input("Issued : (Y/y for True anything else for false)")
    issued= (issued=="y" or issued == "y")
    author = input("Author name: ")
    year= int(input("Year: "))

    return {
        'Id' : id,
        'name': name,
        'description': description,
        'isbn': isbn,
        'page_count':page_count,
        'issued':issued,
        'author':author,
        'year': year
    
        }

#create book function
def create_book():
    print("Plaase enter your book information")
    book_input=input_book_info()
    book = Book(book_input['Id'],book_input['name'],
                book_input['description'], book_input['isbn'],
                  book_input['page_count'],book_input['issued'],
                  book_input['author'], book_input['year'])
    return book

# defining save_books
def save_books(books):
    _json_books=[]
    for book in books:
        _json_books.append(book.to_dict())
    try:
        file = open("books.json","w")
        file.write(json.dumps(_json_books,indent=4))
    except:
        print("we had an error saving books")

#load books function
def load_books():
    try:
        file = open("books.json","r")
        loaded_books = json.loads(file.read())
        books=[]
        for book in loaded_books:
            new_obj= Book(book['Id'],book['name'],
                            book['description'], book['isbn'],
                            book_input['page_count'],book['issued'],
                            book['author'], book['year'])
            books.append(new_obj)
        print("Books are loaded")
        return books
        
    except:
       print("given file dosen't exist or error")

#find books function
def find_book(books, id):
    for index,book in enumerate(books):
        if book.id==id:
            return index
    return None

#issue book function
def issue_book(B1, id):
    Print(True) if find_book(B1, id)!=None else print(False)
