import books
import members
import transactions

def main_menu():
    while True:
        print("\nLibrary Menu")
        print("1. Books Menu")
        print("2. Members Menu")
        print("3. Transactions Menu")
        print("4. Reports Menu")
        print("5. Exit")
        choice = input("Choice [1-5]: ")
        if choice == '1':
            books.books_menu()
        elif choice == '2':
            members.members_menu()
        elif choice == '3':
            transactions.transactions_menu()
        elif choice == '4':
            reports_menu()
        elif choice == '5':
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

def reports_menu():
    while True:
        print("\nReports Menu")
        print("1. All Books List")
        print("2. All Members List")
        print("3. Book Search")
        print("4. Member Search")
        print("5. Issue Status")
        print("6. Return")
        choice = input("Choice [1-6]: ")
        if choice == '1':
            books.show_books()
        elif choice == '2':
            members.show_members()
        elif choice == '3':
            books.find_book()
        elif choice == '4':
            members.find_member()
        elif choice == '5':
            transactions.issue_status()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
