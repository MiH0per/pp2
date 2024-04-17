import psycopg2
from config import load_config

def update_contact(contact_id, new_first_name=None, new_last_name=None, new_phone_number=None):
    """ Update a contact in the contacts table """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if new_first_name:
                    cur.execute("UPDATE contacts SET first_name = %s WHERE id = %s", (new_first_name, contact_id))
                if new_last_name:
                    cur.execute("UPDATE contacts SET last_name = %s WHERE id = %s", (new_last_name, contact_id))
                if new_phone_number:
                    cur.execute("UPDATE contacts SET phone_number = %s WHERE id = %s", (new_phone_number, contact_id))
                print("Contact updated successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    contact_id = int(input("Enter the contact ID to update: "))
    new_first_name = input("Enter new first name (leave blank to keep unchanged): ")
    new_last_name = input("Enter new last name (leave blank to keep unchanged): ")
    new_phone_number = input("Enter new phone number (leave blank to keep unchanged): ")
    update_contact(contact_id, new_first_name, new_last_name, new_phone_number)
    input("Press Enter to exit...")
