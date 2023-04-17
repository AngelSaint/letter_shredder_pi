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

# Define a function to execute SQL queries and return results
def execute_query(query):
  cursor = mydb.cursor()
  cursor.execute(query)
  result = cursor.fetchall()
  return result

# Define a route to display the search form
@app.route('/')
def search_form():
    return render_template('search.html')

# Define a route to handle search requests
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_text = request.form['search_text']
        search_results = []

        # Execute SQL queries to search for the search_text in each table
        query1 = "SELECT * FROM Residents WHERE Name LIKE '%" + search_text + "%'"
        query2 = "SELECT * FROM BlackList WHERE Name LIKE '%" + search_text + "%'"
        result1 = execute_query(query1)
        result2 = execute_query(query2)

        # Add the search results to the search_results list
        if result1:
            search_results.append(('Residents', result1))
        if result2:
            search_results.append(('BlackList', result2))

        # Render the search results template
        return render_template('search_results.html', search_text=search_text, search_results=search_results)

    # If the request method is GET, display the search form
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)