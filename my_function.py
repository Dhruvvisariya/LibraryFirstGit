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
        'id' : id,
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
    book = Book(book_input['id'],book_input['name'],
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
import json

# load books function
def load_books():
    try:
        with open("books.json", "r") as file:
            loaded_books = json.loads(file.read())
            books = []
            for book in loaded_books:
                new_obj = Book(book['id'], book['name'],
                               book['description'], book['isbn'],
                               book['page_count'], book['issued'],
                               book['author'], book['year'])
                books.append(new_obj)
            print("Books are loaded")
            return books
            
    except FileNotFoundError:
        print("The file 'books.json' doesn't exist.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
    except KeyError as e:
        print(f"Key error: {e}. Please check if all keys exist in the JSON data.")
    except Exception as e:
        print(f"An error occurred: {e}")


#find books function
def find_book(books, id):
    for index,book in enumerate(books):
        if book.id==id:
            return index
    return None

#issue book function
def issue_book(Books, id):
    index= find_book(Books, id)
    if index!=None:
        Books[index].issued=True
        print("Book is issued!")
    else:
        print("No book  found !")
     

#return book funtion
def return_book(Books, id):
    index= find_book(Books, id)
    if index!=None:
        Books[index].issued=False
        print("Book is returned")
    else:
        print("No book  found !")

#update book function
def update_book(books):
    ID= input ( "Entre ID :")
    Index = find_book(books,ID)
    if Index != None:
        NewBook= create_book()
        books[Index]= NewBook
    else:
        print("No such book")

#show all books function
def show_all(books):
    for book in books:
        print(book.to_dict())
    
#show a book fucntion
def show_book(books):
    ID=input("Enter ID :")
    index=find_book(books,ID)
    if index != None:
        print(books[index].to_dict())
    else:
        print("No such book")

