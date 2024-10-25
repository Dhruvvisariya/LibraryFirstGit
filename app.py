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
        print(my_function.load_books())
    else:
        print("wrong command")
    input("press enter to continue ...")
    
    os.system("cls")
    my_function.print_options()
    option= input()