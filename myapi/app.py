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



# Route for creating a new alert
@app.route('/alerts', methods=['POST'])
def create_alert():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    conn = sqlite3.connect('myapi/database/alerts.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO alerts (message) VALUES (?)', (message,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Alert created successfully'}), 201


