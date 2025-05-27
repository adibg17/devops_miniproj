from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("contact.db") as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            message TEXT
        )""")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    with sqlite3.connect("contact.db") as conn:
        conn.execute("INSERT INTO contacts (name, email, phone, message) VALUES (?, ?, ?, ?)", 
                     (name, email, phone, message))
    return redirect('/contacts')

@app.route('/contacts')
def contacts():
    with sqlite3.connect("contact.db") as conn:
        rows = conn.execute("SELECT * FROM contacts").fetchall()
    return render_template('contacts.html', contacts=rows)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
