import psycopg2
from config import load_config

def insert_data_from_console():
    """ Insert data from console into the contacts table """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                phone_number = input("Enter phone number: ")
                cur.execute("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))
                print("Data inserted successfully from console.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    insert_data_from_console()
    input("Press Enter to exit...")
