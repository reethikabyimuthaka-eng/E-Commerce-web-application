from flask import Flask, render_template, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# Function to connect to database
def get_db():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    return conn

# Homepage: show products
@app.route("/")
def home():
    db = get_db()
    products = db.execute("SELECT * FROM products").fetchall()
    return render_template("index.html", products=products)

# Add product to cart
@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]
    cart.append(id)
    session["cart"] = cart

    return redirect("/")

# View cart
@app.route("/cart")
def cart():
    db = get_db()
    ids = session.get("cart", [])

    products = []
    for pid in ids:
        product = db.execute("SELECT * FROM products WHERE id=?", (pid,)).fetchone()
        if product:
            products.append(product)

    return render_template("cart.html", products=products)

# Checkout
@app.route("/checkout")
def checkout():
    session["cart"] = []
    return "Order placed successfully!"

if __name__ == "__main__":
    # Run on port 8000 to avoid conflicts
    app.run(host="0.0.0.0", port=5000, debug=True)
