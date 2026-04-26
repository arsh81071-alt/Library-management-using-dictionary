from utils import books, issued_books
from datetime import datetime
from fine_calculator import calculate_fine

def return_book():
    print("\nRETURN BOOK")

    book_id = input("Enter Book ID: ").strip()

    if book_id not in issued_books:
        print("Invalid Book ID or not issued!")
        return

    data = issued_books[book_id]

    today = datetime.now()
    due_date = data["return_date"]

    extra_days = (today - due_date).days

    fine = 0
    if extra_days > 0:
        fine = calculate_fine(extra_days)

    books[book_id]["available"] = True
    issued_books.pop(book_id)

    print("\nBook Returned Successfully!")

    if fine > 0:
        print(f"Late by {extra_days} days")
        print(f"Fine to pay: ₹{fine}")
    else:
        print("Returned on time. No fine!")