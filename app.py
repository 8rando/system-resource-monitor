from flask import Flask,render_template
import sqlite3

app = Flask(__name__)

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('resources.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usage ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return data


@app.route("/")
def dashboard():
    data = fetch_data()
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)