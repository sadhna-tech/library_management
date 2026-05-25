import json
import os

FILE_NAME = "books.json"


# Load books
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save books
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# Add book
def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)
    save_books(books)

    print("Book added successfully!\n")


# View books
def view_books(books):
    if not books:
        print("No books available.\n")
        return

    print("\nBook List:")
    
    for index, book in enumerate(books, start=1):
        status = "Issued" if book["issued"] else "Available"

        print(f"{index}. {book['title']} by {book['author']} - {status}")

    print()


# Search book
def search_book(books):
    name = input("Enter book title to search: ")

    found = False

    for book in books:
        if book["title"].lower() == name.lower():
            print(f"Found: {book}")
            found = True

    if not found:
        print("Book not found.\n")


# Issue book
def issue_book(books):
    name = input("Enter book title to issue: ")

    for book in books:
        if book["title"].lower() == name.lower():

            if book["issued"]:
                print("Book already issued.\n")

            else:
                book["issued"] = True
                save_books(books)

                print("Book issued successfully!\n")

            return

    print("Book not found.\n")


# Main menu
def main():
    books = load_books()

    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            search_book(books)

        elif choice == "4":
            issue_book(books)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()