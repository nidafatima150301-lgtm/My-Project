class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        book_id = int(input("Enter Book ID: "))

        if book_id in self.books:
            print("Book ID already exists!")
            return

        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        self.books[book_id] = {
            "Book Name": name,
            "Author": author
        }

        print("Book Added Successfully!")

    def view_books(self):
        if len(self.books) == 0:
            print("No Books Available.")
            return

        print("\n----- Book List -----")
        for book_id, details in self.books.items():
            print(f"Book ID : {book_id}")
            print(f"Book Name : {details['Book Name']}")
            print(f"Author : {details['Author']}")
            print("---------------------")

    def search_book(self):
        book_id = int(input("Enter Book ID to Search: "))

        if book_id in self.books:
            print("Book Found!")
            print("Book Name :", self.books[book_id]["Book Name"])
            print("Author :", self.books[book_id]["Author"])
        else:
            print("Book Not Found!")

    def delete_book(self):
        book_id = int(input("Enter Book ID to Delete: "))

        if book_id in self.books:
            del self.books[book_id]
            print("Book Deleted Successfully!")
        else:
            print("Book Not Found!")

obj = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        obj.add_book()
    elif choice == 2:
        obj.view_books()
    elif choice == 3:
        obj.search_book()
    elif choice == 4:
        obj.delete_book()
    elif choice == 5:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")