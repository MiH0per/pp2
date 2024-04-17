import psycopg2
import csv
from config import load_config

def insert_data_from_csv(file_path):
    """ Insert data from a CSV file into the contacts table """
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        cur.execute("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)", row)
                print("Data inserted successfully from CSV.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    file_path = input("Path to your csv file: ")
    insert_data_from_csv(file_path)
    input("Press Enter to exit...")
