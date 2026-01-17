import requests
import sqlite3

# Example API endpoint
api_url = "https://example.com/api/books"

# Fetching the data from the API
response = requests.get(api_url)


# API gives a json response
books_data = response.json()   

# Connecting to SQLite database (or create it if it doesn't exist)
database = sqlite3.connect("books.db")
cursor = database.cursor()

# Creating books table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

# Inserting API data into database
for book in books_data:
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (book["title"], book["author"], book["year"])
    )

database.commit()

# Fetching and displaying data
cursor.execute("SELECT * FROM books")
all_books = cursor.fetchall()

print("Books stored in database:")
for book in all_books:
    print(book)

database.close()
