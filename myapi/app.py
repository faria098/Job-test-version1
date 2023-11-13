from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database connection
def init_db():
    conn = sqlite3.connect('myapi/database/alerts.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

