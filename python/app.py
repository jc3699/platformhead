from flask import Flask, render_template, request, redirect
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Database connection using .env credentials
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT", 3306))
)
cursor = conn.cursor(dictionary=True)

# Home route: display tasks
@app.route('/')
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

# Add a task
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()
    return redirect('/')

# Delete a task
@app.route('/delete/<int:id>')
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
