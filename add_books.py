from utils import books

def add_book():
    print("\nADD NEW BOOK")

    book_id = input("Enter Book ID: ").strip()
    name = input("Enter Book Name: ").strip()
    author = input("Enter Author Name: ").strip()

    if book_id in books:
        print("Book ID already exists!")
        return

    books[book_id] = {
        "name": name,
        "author": author,
        "available": True
    }

    print("Book added successfully!")