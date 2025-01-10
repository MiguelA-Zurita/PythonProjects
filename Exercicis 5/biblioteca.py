class book:
    def __init__(self, title, author, year, id):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return (f"{self.title} - {self.author} - {self.year}")

biblioteca = {

}

def menu():
    print("1. Add a book")
    print("2. Search a book")
    print("3. Delete a book")
    print("4. List all books")
    print("5. Exit")
    option = int(input("Choose an option: \n"))
    if option == 1:
        title = input("Enter the title of the book: \n")
        author = input("Enter the author of the book: \n")
        year = input("Enter the year of the book: \n")
        add_book( title, author, year)
    elif option == 2:
        book = input("Enter the title of the book: \n")
        search_book(book)
    elif option == 3:
        book = input("Enter the title of the book: \n")
        delete_book(book)
    elif option == 4:
        list_books()
    elif option == 5:
        exit
    else:
        print("Invalid option")
        menu()

def add_book(titulo, autor, any):
    id = len(biblioteca)
    biblioteca[id] = book(titulo, autor, any, id)
    print("Book added")
    menu()

def search_book(book):
    for i in biblioteca:
        if biblioteca[i].title == book:
            print(biblioteca[i])
            menu()
        else:
            print("Book not found")
            menu()

def delete_book(book):
    for i in biblioteca:
        if biblioteca[i].title == book:
            del biblioteca[i]
            print("Book deleted")
            menu()
        else:
            print("Book not found")
            menu()
    print("There aren't any books to delete!")
    menu()

def list_books():
    for i in biblioteca:
        print(biblioteca[i])
    menu()

if __name__ == "__main__":
    menu()