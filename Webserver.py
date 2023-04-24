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


@app.route("/residents")
def residents():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Residents")
    residents = cursor.fetchall()
    return render_template("residents.html", residents=residents)


@app.route("/add_resident", methods=["POST"])
def add_resident():
    name = request.form["name"]
    address = request.form["address"]
    box = request.form["box"]
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Residents (Name, Address, `Box #`) VALUES (%s, %s, %s)", (name, address, box))
    mydb.commit()
    return residents()


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


# def run():
if __name__ == '__main__':
    app.run(host="0.0.0.0")