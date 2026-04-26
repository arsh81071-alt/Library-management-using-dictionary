from utils import books

def show_book():
    print("\nLIBRARY BOOK LIST")

    if not books:
        print("No books available.")
        return

    for book_id, details in books.items():
        status = "Available" if details ["available"] else "Issued"

        print("\n----------------------------")
        print(f"Book ID   : {book_id}")
        print(f"Name      : {details['name']}")
        print(f"Author    : {details['author']}")
        print(f"Status    : {status}")
    print("----------------------------")