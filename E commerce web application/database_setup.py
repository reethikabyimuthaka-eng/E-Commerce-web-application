import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
price INTEGER
)
""")

# Add products
cursor.execute("INSERT INTO products(name,price) VALUES('Laptop',800)")
cursor.execute("INSERT INTO products(name,price) VALUES('Phone',500)")
cursor.execute("INSERT INTO products(name,price) VALUES('Headphones',100)")

conn.commit()
conn.close()

print("Database created successfully")
