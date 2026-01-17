import csv
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
database = sqlite3.connect("users.db")
cursor = database.cursor()

# Creating the users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

# Read data from CSV file and insert into the database
with open("users.csv", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

database.commit()

# Display stored users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("Users stored in database:")
for user in users:
    print(user)

database.close()
