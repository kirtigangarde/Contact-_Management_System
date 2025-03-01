import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the file."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print("-" * 20)

def main():
    """Main function to run the contact management program."""
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()