import psycopg2
from config import load_config

def query_contacts(filter_by=None, value=None):
    """ Query contacts from the contacts table """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if filter_by and value:
                    cur.execute(f"SELECT * FROM contacts WHERE {filter_by} = %s", (value,))
                else:
                    cur.execute("SELECT * FROM contacts")
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    filter_by = input("Enter filter column name (leave blank to retrieve all contacts): ")
    value = input(f"Enter value to filter by {filter_by} (leave blank to retrieve all contacts): ") if filter_by else None
    query_contacts(filter_by, value)
    input("Press Enter to exit...")
