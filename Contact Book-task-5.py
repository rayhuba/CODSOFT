#List to store contacts
contacts=[]
# add contact
def add_contact(name, phone_number, email, address):
    contact = {
        "name": name,
        "phone_number": phone_number,
        "email":email,
        "address":address
    }
    contacts.append(contact)
    print("Contact added successfully!")

#View Contact list function
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}")

def search_contact(search_term):
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']]
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(name, new_phone_number=None, new_email=None, new_address=None):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if new_phone_number:
                contact['phone_number'] = new_phone_number
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    print("Contact deleted successfully!")

def menu():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            new_phone_number = input("Enter new phone number (leave empty to keep current): ")
            new_email = input("Enter new email (leave empty to keep current): ")
            new_address = input("Enter new address (leave empty to keep current): ")
            update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Start the program
menu()
    