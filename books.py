import json
from utils import clear_screen, get_input

BOOKS_FILE = "books.json"

def load_books():
    try:
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=2)

def new_book():
    clear_screen()
    print("New Book Details")
    book = {
        "BookId": int(get_input("Enter BookId: ")),
        "BName": get_input("Enter Book Name: "),
        "Publisher": get_input("Enter Publisher Name: "),
        "Author": get_input("Enter Author Name: "),
        "Pages": int(get_input("Enter Pages: ")),
        "Price": int(get_input("Enter Price: ")),
        "Qty1": int(get_input("Actual Quantity: ")),
    }
    book["Qty2"] = book["Qty1"]
    book["Status"] = 1
    books = load_books()
    books.append(book)
    save = get_input("Save the record [Y/N]: ").lower()
    if save == 'y':
        save_books(books)
        print("Record saved successfully")
    else:
        print("Record not saved.")

def edit_book_info():
    clear_screen()
    print("Edit Book")
    books = load_books()
    book_id = int(get_input("Enter BookId: "))
    found = False
    for book in books:
        if book["BookId"] == book_id:
            found = True
            print(f"Present Data: {book}")
            book["BName"] = get_input("New Book Name: ")
            book["Publisher"] = get_input("Publisher: ")
            book["Author"] = get_input("Author: ")
            book["Pages"] = int(get_input("Pages: "))
            book["Price"] = int(get_input("Price: "))
            print("Record modified.")
            break
    if found:
        save_books(books)
    else:
        print("Record not found.")

def find_book():
    clear_screen()
    books = load_books()
    book_id = int(get_input("Enter BookId: "))
    for book in books:
        if book["BookId"] == book_id:
            print(book)
            return
    print("Record not found.")

def show_books():
    clear_screen()
    books = load_books()
    if not books:
        print("No books available.")
        return
    for book in books:
        print(book)

def is_book_available(book_id):
    books = load_books()
    for book in books:
        if book["BookId"] == book_id and book["Qty2"] > 0:
            print(f"Book: {book['BName']}, Publisher: {book['Publisher']}, Author: {book['Author']}")
            return True
    return False

def change_qty2(book_id, delta):
    books = load_books()
    for book in books:
        if book["BookId"] == book_id:
            book["Qty2"] += delta
            save_books(books)
            break

def books_menu():
    while True:
        print("\nBooks Menu")
        print("1. New Book")
        print("2. Edit Book Info")
        print("3. Find Book")
        print("4. Show Books")
        print("5. Return")
        choice = get_input("Choice [1-5]: ")
        if choice == '1':
            new_book()
        elif choice == '2':
            edit_book_info()
        elif choice == '3':
            find_book()
        elif choice == '4':
            show_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
