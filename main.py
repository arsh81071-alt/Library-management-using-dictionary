from add_books import add_book
from show_books import show_book
from issue_books import issue_book
from return_books import return_book

def library():

    menu = {
        1: add_book,
        2: show_book,
        3: issue_book,
        4: return_book
    }

    while True:
        print("\n========== LIBRARY MENU ==========")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if not choice.isdigit():
            print("Please enter a valid number!")
            continue

        choice = int(choice)

        if choice in menu:
            menu[choice]()
        elif choice == 5:
            print("\nThank you for using Library System!")
            break
        else:
            print("Invalid choice!")

library()