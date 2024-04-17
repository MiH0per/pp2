import csv
from create_tables import create_tables
from insert_data_from_csv import insert_data_from_csv
from insert_from_console import insert_data_from_console
from update_contact import update_contact
from query_contacts import query_contacts
from delete_contact import delete_contact_by_username
from show_table import query_all_contacts
def print_menu():
    """ Print menu options """
    print("\nPhonebook")
    print("1. Create Contacts Table")
    print("2. Insert Data from CSV")
    print("3. Insert Data from Console")
    print("4. Update Contact")
    print("5. Query Contacts")
    print("6. Delete Contact by Username")
    print("7. Show the Table")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_tables()
        elif choice == '2':
            file_path = input("Enter CSV file path: ")
            insert_data_from_csv(file_path)
        elif choice == '3':
            insert_data_from_console()
        elif choice == '4':
            old_first_name = input("Enter old first name of the contact: ")
            old_last_name = input("Enter old last name of the contact: ")
            new_first_name = input("Enter new first name (leave blank to keep unchanged): ")
            new_last_name = input("Enter new last name (leave blank to keep unchanged): ")
            new_phone_number = input("Enter new phone number (leave blank to keep unchanged): ")
            update_contact(old_first_name, old_last_name, new_first_name, new_last_name, new_phone_number)
        elif choice == '5':
            filter_by = input("Enter filter column name (leave blank to retrieve all contacts): ")
            value = input(f"Enter value to filter by {filter_by} (leave blank to retrieve all contacts): ") if filter_by else None
            query_contacts(filter_by, value)
        elif choice == '6':
            first_name = input("Enter first name of the contact to delete: ")
            last_name = input("Enter last name of the contact to delete: ")
            delete_contact_by_username(first_name, last_name)
        elif choice == '7':
            query_all_contacts()

        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
