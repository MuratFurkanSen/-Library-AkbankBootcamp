from library import Library

lib = Library()
# Printed menu just once for better view (in my opinion)
menu_str = """*** MENU***
1) List Books
2) Add Book
3) Remove Book
4) Quit"""
print(menu_str)
while True:
    # Take and get an action for user input
    command = input("Pls enter command: ")
    if command == "1":
        lib.listBooks()
    elif command == "2":
        lib.addBook()
    elif command == "3":
        lib.removeBook()
    elif command == "4":
        break
    else:
        print("You have entered an invalid command.")
