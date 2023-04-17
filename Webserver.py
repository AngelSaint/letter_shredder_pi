from flask import Flask, render_template, request
import mysql.connector

# Create a Flask app
app = Flask(__name__)

# Establish a connection to the MariaDB SQL database
conn = mysql.connector.connect(
    user="angelos4",
    password="12345678",
    host="localhost",
    database="letter_shredder"
)


# Define the function for the index page
@app.route("/")
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Residents")
    rows = cur.fetchall()
    return render_template("index.html", rows=rows)


# Define the function for the home page
@app.route("/home")
def home():
    cur = conn.cursor()
    cur.execute("SELECT * FROM BlackList")
    rows = cur.fetchall()
    return render_template("home.html", rows=rows)


# Define the function for the search page
@app.route("/search")
def search():
    query = request.args.get("q")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM BlackList WHERE Name LIKE '%{query}%'")
    rows = cur.fetchall()
    return render_template("search.html", rows=rows)


if __name__ == "__main__":
    app.run()