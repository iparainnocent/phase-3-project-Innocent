import sqlite3

def init_db():
    connection = sqlite3.connect('rental_system.db')
    cursor = connection.cursor()

    # Create Customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    # Create Movies table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL
    )
    ''')

    # Create Rentals table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rentals (
        customer_id INTEGER,
        movie_id INTEGER,
        rental_date TEXT NOT NULL,
        PRIMARY KEY (customer_id, movie_id),
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )
    ''')

    connection.commit()
    connection.close()