import json
import books
import members
from utils import clear_screen, get_input

TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    try:
        with open(TRANSACTIONS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as f:
        json.dump(transactions, f, indent=2)

def book_issue():
    clear_screen()
    print("Book Issue")
    mem_id = int(get_input("Enter Member Id: "))
    if not members.is_member(mem_id):
        print("Member not eligible or not found.")
        return
    book_id = int(get_input("Enter Book Id: "))
    if not books.is_book_available(book_id):
        print("Book not available.")
        return
    issue_date = get_input("Enter Issue Date (YYYY-MM-DD): ")
    confirm = get_input("Issue Book [Y/N]: ").lower()
    if confirm == "y":
        transactions = load_transactions()
        transactions.append({"MemId": mem_id, "BookId": book_id, "IssueDate": issue_date, "ReturnDate": ""})
        save_transactions(transactions)
        members.change_bcount(mem_id, 1)
        books.change_qty2(book_id, -1)
        print("Book issued successfully.")

def book_return():
    clear_screen()
    print("Book Return")
    mem_id = int(get_input("Enter Member Id: "))
    book_id = int(get_input("Enter Book Id: "))
    transactions = load_transactions()
    for t in transactions:
        if t["MemId"] == mem_id and t["BookId"] == book_id and t["ReturnDate"] == "":
            return_date = get_input("Enter Return Date (YYYY-MM-DD): ")
            t["ReturnDate"] = return_date
            save_transactions(transactions)
            members.change_bcount(mem_id, -1)
            books.change_qty2(book_id, 1)
            print("Book returned successfully.")
            return
    print("No matching issued book found.")

def issue_status():
    clear_screen()
    print("Issue Status")
    transactions = load_transactions()
    if not transactions:
        print("No transactions yet.")
        return
    for t in transactions:
        print(t)

def transactions_menu():
    while True:
        print("\nTransactions Menu")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Return")
        choice = get_input("Choice [1-3]: ")
        if choice == '1':
            book_issue()
        elif choice == '2':
            book_return()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")
