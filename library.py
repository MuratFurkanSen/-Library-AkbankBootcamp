class Library:
    def __init__(self):
        # Opening connection with initialize
        self.data_file = open("books.txt", "a+", encoding="utf-8")

    def __del__(self):
        # Close connection with end of the library program
        self.data_file.close()

    def listBooks(self):
        # Get cursor to beginning of the file
        self.data_file.seek(0)

        # Get book data as lines
        books_data = self.data_file.read().splitlines()

        # We only need name and author so filter them
        info = [i.split(",")[:2] for i in books_data]
        print("Current Book(s) in Library:")
        print()

        # Print books
        for name, author in info:
            print(f"Name: {name}, Author: {author}")

    def addBook(self):
        # Get necessary variables
        name = input("Pls enter the book's name: ")
        author = input("Pls enter the book's author:")
        release = input("Pls enter the book's release year: ")
        pages = input("Pls enter the number of pages book has: ")

        # Set info for saving to file
        book_info = f"{name},{author},{release},{pages}\n"
        self.data_file.write(book_info)

    def removeBook(self):
        # Get necessary variables
        name = input("Pls enter the book's name you want to delete: ")
        author = input("Pls enter the book's author you want to delete: ")

        # Get cursor to beginning of the file
        self.data_file.seek(0)

        # Get book data as lines
        books_data = self.data_file.read().splitlines()

        # Filter the book will be deleted from data
        info = [i + "\n" for i in books_data if i.split(",")[0] != name or i.split(",")[1] != author]
        self.data_file.close()

        # To overwrite open the file with "w" mode
        self.data_file = open("books.txt", "w", encoding="utf-8")

        # Write remaining books
        self.data_file.write("".join(info))
        self.data_file.close()

        # Set file mode for read and write mode again
        self.data_file = open("books.txt", "a+", encoding="utf-8")