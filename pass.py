import sqlite3
import getpass
import hashlib

# Function to create a new password database
def create_database():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()     #To execute SQL Queries
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (website TEXT PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new password
def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # Hash the password before storing it (you should use a stronger hashing algorithm)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords VALUES (?, ?, ?)", (website, username, hashed_password))
    conn.commit()
    conn.close()

# Function to retrieve a password
def get_password():
    website = input("Enter website: ")

    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM passwords WHERE website=?", (website,))
    result = cursor.fetchone()

    if result:
        print("Password:", result[0])
    else:
        print("Website not found in the database.")
    
    conn.close()

# Main program loop
def main():
    create_database()
    while True:
        print("\nOptions:")
        print("1. Add a password")
        print("2. Retrieve a password")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":         #always executed
    main()
