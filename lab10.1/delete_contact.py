import psycopg2
from config import load_config

def delete_contact_by_username(first_name, last_name):
    """ Delete a contact from the contacts table by username """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM contacts WHERE first_name = %s AND last_name = %s", (first_name, last_name))
                if cur.rowcount > 0:
                    print("Contact deleted successfully.")
                else:
                    print("Contact not found.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    first_name = input("Enter first name of the contact to delete: ")
    last_name = input("Enter last name of the contact to delete: ")
    delete_contact_by_username(first_name, last_name)
    input("Press Enter to exit...")
