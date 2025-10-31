import json
from utils import clear_screen, get_input

MEMBERS_FILE = "members.json"

def load_members():
    try:
        with open(MEMBERS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_members(members):
    with open(MEMBERS_FILE, "w") as f:
        json.dump(members, f, indent=2)

def new_member():
    clear_screen()
    print("New Member Details")
    member = {
        "MemId": int(get_input("Enter MemberId: ")),
        "MemName": get_input("Enter Member Name: "),
        "Location": get_input("Enter Location: "),
        "Phone": get_input("Enter Phone Number: "),
        "Email": get_input("Enter Email Id: "),
        "Bcount": 0,
        "Status": 1
    }
    members = load_members()
    save = get_input("Save the record [Y/N]: ").lower()
    if save == 'y':
        members.append(member)
        save_members(members)
        print("Record saved successfully")
    else:
        print("Record not saved.")

def edit_member_info():
    clear_screen()
    print("Edit Member")
    members = load_members()
    mem_id = int(get_input("Enter MemberId: "))
    found = False
    for member in members:
        if member["MemId"] == mem_id:
            found = True
            print(f"Present Data: {member}")
            member["MemName"] = get_input("New Member Name: ")
            member["Location"] = get_input("Location: ")
            member["Phone"] = get_input("Phone: ")
            member["Email"] = get_input("Email Id: ")
            print("Record modified.")
            break
    if found:
        save_members(members)
    else:
        print("Record not found.")

def find_member():
    clear_screen()
    members = load_members()
    mem_id = int(get_input("Enter MemberId: "))
    for member in members:
        if member["MemId"] == mem_id:
            print(member)
            return
    print("Record not found.")

def show_members():
    clear_screen()
    members = load_members()
    if not members:
        print("No members available.")
        return
    for member in members:
        print(member)

def is_member(mem_id):
    members = load_members()
    for member in members:
        if member["MemId"] == mem_id and member["Bcount"] < 3:
            print(f"Member: {member['MemName']}, Location: {member['Location']}, Phone: {member['Phone']}")
            return True
    return False

def change_bcount(mem_id, delta):
    members = load_members()
    for member in members:
        if member["MemId"] == mem_id:
            member["Bcount"] += delta
            save_members(members)
            break

def members_menu():
    while True:
        print("\nMembers Menu")
        print("1. New Member")
        print("2. Edit Member Info")
        print("3. Find Member")
        print("4. Show Members")
        print("5. Return")
        choice = get_input("Choice [1-5]: ")
        if choice == '1':
            new_member()
        elif choice == '2':
            edit_member_info()
        elif choice == '3':
            find_member()
        elif choice == '4':
            show_members()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
