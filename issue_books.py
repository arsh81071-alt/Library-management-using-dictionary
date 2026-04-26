from utils import books, issued_books
from datetime import datetime, timedelta

def issue_book():
    print("\nISSUE BOOK")

    book_id = input("Enter Book ID: ").strip()

    if book_id not in books:
        print("Book not found!")
        return

    if not books[book_id]["available"]:
        print("Book already issued!")
        return

    student = input("Enter Student Name: ").strip()

    try:
        days = int(input("Enter number of days to issue: "))
    except:
        print("Invalid number!")
        return

    issue_date = datetime.now()
    return_date = issue_date + timedelta(days=days)

    books[book_id]["available"] = False

    issued_books[book_id] = {
        "student": student,
        "issue_date": issue_date,
        "return_date": return_date,
        "days": days
    }

    print("\nBook Issued Successfully!")
    print(f"Return before: {return_date.date()}")

    print("\nFine Rules:")
    print("1st Week  : ₹10/day")
    print("2nd Week  : ₹20/day")
    print("3rd Week  : ₹30/day ... and so on")