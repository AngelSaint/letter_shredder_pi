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
    apartment = request.form["apartment"]
    box = request.form["box"]
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO Residents (Name, Address, Apartment, `Box#`) VALUES (%s, %s, %s, %s)", (name, address, apartment, box))
    mydb.commit()
    return residents()


@app.route("/remove_resident", methods=["POST"])
def remove_resident():
    name = request.form["remove_name"]
    address = request.form["remove_address"]
    apartment = request.form["remove_apartment"]
    box = request.form["remove_box"]
    cursor = mydb.cursor()
    print(name, address, apartment, box)

    cursor.execute("DELETE FROM Residents WHERE Name = %s AND Address = %s  AND Apartment= %s  AND `Box#`= %s", (name, address, apartment, box))
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
    blacklist = mycursor.fetchall()
    # Render the blacklist.html template and pass the results as a parameter
    return render_template('blacklist.html', blacklist=blacklist)


@app.route("/add_blacklist", methods=["POST"])
def add_blacklist():
    name = request.form["name"]
    box1 = 1 if request.form.get("box1") else 0
    box2 = 1 if request.form.get("box2") else 0
    box3 = 1 if request.form.get("box3") else 0
    print(box1, box2, box3)
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO BlackList (Name, `Box1`, `Box2`, `Box3`) VALUES (%s, %s, %s, %s)", (name, box1, box2, box3))
    mydb.commit()
    return show_blacklist()


@app.route("/remove_blacklist", methods=["POST"])
def remove_blacklist():
    name = request.form["remove_name"]
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM BlackList WHERE Name = %s", (name, ))
    mydb.commit()
    return show_blacklist()


# def run():
if __name__ == '__main__':
    app.run(host="0.0.0.0")