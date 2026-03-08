import sqlite3

# Database connection
conn = sqlite3.connect("cloud_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
phone TEXT UNIQUE NOT NULL
)
""")

# Function to add user
def add_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    try:
        cursor.execute(
            "INSERT INTO users(name,email,phone) VALUES(?,?,?)",
            (name,email,phone)
        )
        conn.commit()
        print("✅ Data stored successfully")

    except sqlite3.IntegrityError:
        print("⚠ Duplicate data detected! Entry rejected.")

# Function to view users
def view_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    if rows:
        print("\nStored Records")
        print("---------------------------")
        for row in rows:
            print("ID:",row[0],"Name:",row[1],"Email:",row[2],"Phone:",row[3])
    else:
        print("No records found")

# Main menu
while True:
    print("\n==== Data Redundancy Removal System ====")
    print("1. Add User Data")
    print("2. View Stored Data")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        view_users()

    elif choice == "3":
        print("System Closed")
        break

    else:
        print("Invalid choice")

conn.close()