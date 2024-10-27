import my_function
import os
my_function.print_options()
option=input()
books =[]
while option !='x' and option !='X':
    if option =='1':
        books.append(my_function.create_book())
    elif option=="2":
        my_function.save_books(books)
    elif option=="3":
        books= my_function.load_books()
    elif option=="4":
        ID=input("Enter ID:")
        my_function.issue_book(books,ID)
    elif option=="5":
        ID=input("Enter ID:")
        my_function.return_book(books,ID)
    elif option=="6":
        my_function.update_book(books)
    elif option=="7":
        my_function.show_all(books)
    elif option=="8":
        my_function.show_book(books)
    else:
        print("wrong command")
    input("press enter to continue ...")
    
    os.system("cls")
    my_function.print_options()
    option= input()