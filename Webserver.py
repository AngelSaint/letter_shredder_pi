from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Define MySQL database connection details
mydb = mysql.connector.connect(
  host="localhost",
  user="angelos4",
  password="12345678",
  database="letter_shredder"
)

# Define a route to show all the entries in the Residents table
@app.route('/residents')
def show_residents():
    # Create a cursor to execute SQL queries
    mycursor = mydb.cursor()
    # Execute a query to select all the entries in the Residents table
    mycursor.execute("SELECT * FROM Residents")
    # Fetch all the results
    results = mycursor.fetchall()
    # Render the residents.html template and pass the results as a parameter
    return render_template('residents.html', results=results)

# Define a route to show all the entries in the BlackList table
@app.route('/blacklist')
def show_blacklist():
    # Create a cursor to execute SQL queries
    mycursor = mydb.cursor()
    # Execute a query to select all the entries in the BlackList table
    mycursor.execute("SELECT * FROM BlackList")
    # Fetch all the results
    results = mycursor.fetchall()
    # Render the blacklist.html template and pass the results as a parameter
    return render_template('blacklist.html', results=results)

if __name__ == '__main__':
    app.run(host="0.0.0.0")