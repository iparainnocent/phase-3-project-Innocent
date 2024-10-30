import sqlite3
from database import init_db

def add_customer(name):
    connection = sqlite3.connect('rental_system.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO customers (name) VALUES (?)', (name,))
    connection.commit()
    connection.close()

def list_customers():
    connection = sqlite3.connect('rental_system.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    connection.close()
    return customers

def add_movie(title, genre):
    connection = sqlite3.connect('rental_system.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO movies (title, genre) VALUES (?, ?)', (title, genre))
    connection.commit()
    connection.close()

def list_movies():
    connection = sqlite3.connect('rental_system.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    connection.close()
    return movies

def rent_movie(customer_id, movie_id, rental_date):
    connection = sqlite3.connect('rental_system.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO rentals (customer_id, movie_id, rental_date) VALUES (?, ?, ?)', (customer_id, movie_id, rental_date))
    connection.commit()
    connection.close()

def list_rentals():
    connection = sqlite3.connect('rental_system.db')
    cursor = connection.cursor()
    cursor.execute('''
    SELECT r.rental_date, c.name, m.title 
    FROM rentals r
    JOIN customers c ON r.customer_id = c.id
    JOIN movies m ON r.movie_id = m.id
    ''')
    rentals = cursor.fetchall()
    connection.close()
    return rentals

def main():
    init_db()  # Initialize the database at the start
    while True:
        print("\nMovie Rental System")
        print("1. Add Customer")
        print("2. List Customers")
        print("3. Add Movie")
        print("4. List Movies")
        print("5. Rent Movie")
        print("6. List Rentals")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter customer name: ")
            add_customer(name)
            print(f'Customer "{name}" added successfully.')
        elif choice == '2':
            customers = list_customers()
            print("Customers:")
            for customer in customers:
                print(customer)
        elif choice == '3':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            add_movie(title, genre)
            print(f'Movie "{title}" added successfully.')
        elif choice == '4':
            movies = list_movies()
            print("Movies:")
            for movie in movies:
                print(movie)
        elif choice == '5':
            customer_id = int(input("Enter customer ID: "))
            movie_id = int(input("Enter movie ID: "))
            rental_date = input("Enter rental date (YYYY-MM-DD): ")
            rent_movie(customer_id, movie_id, rental_date)
            print(f'Movie ID {movie_id} rented to Customer ID {customer_id} on {rental_date}.')
        elif choice == '6':
            rentals = list_rentals()
            print("Rentals:")
            for rental in rentals:
                print(rental)
        elif choice == '7':
            print("Exiting the Movie Rental System.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()