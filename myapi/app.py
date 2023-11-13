from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database connection
def init_db():
    conn = sqlite3.connect('database/alerts.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()



# Route for creating a new alert or updating an existing alert
@app.route('/alerts', methods=['POST'])
def create_or_update_alert():
    data = request.get_json()
    message = data.get('message')
    alert_id = data.get('id')  # Client-specified ID

    print('alert id',alert_id)

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    conn = sqlite3.connect('database/alerts.db')
    cursor = conn.cursor()

    if alert_id is not None:
        print('I have the alert id')
        # Check if the specified ID already exists
        cursor.execute('SELECT * FROM alerts WHERE id = ?', (alert_id,))
        existing_alert = cursor.fetchone()

        if existing_alert:
            # If the ID exists, update the existing alert
            cursor.execute('UPDATE alerts SET message = ? WHERE id = ?', (message, alert_id))
            conn.commit()
            conn.close()
            return jsonify({'message': f'Alert with ID {alert_id} updated successfully'}), 200
        else:
            # If the ID does not exist, create a new alert
            cursor.execute('INSERT INTO alerts (message, id) VALUES (?,?)', (message,alert_id))
            conn.commit()
            conn.close()
            return jsonify({'message': f'Alert with ID {alert_id} created successfully'}), 200


    # If the ID is not specified create a new alert without a id
    cursor.execute('INSERT INTO alerts (message) VALUES (?)', (message,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Alert created successfully'}), 201



# Route for retrieving all alerts
@app.route('/alerts', methods=['GET'])
def get_alerts():
    conn = sqlite3.connect('database/alerts.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM alerts ORDER BY timestamp DESC')
    alerts = cursor.fetchall()

    conn.close()

    alert_list = [{'id': alert[0], 'message': alert[1], 'timestamp': alert[2]} for alert in alerts]

    return jsonify(alert_list)

# Route for retrieving a specific alert by ID
@app.route('/alerts/<int:alert_id>', methods=['GET'])
def get_alert_by_id(alert_id):
    conn = sqlite3.connect('database/alerts.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM alerts WHERE id = ?', (alert_id,))
    alert = cursor.fetchone()

    conn.close()

    if alert is None:
        return jsonify({'error': 'Alert not found'}), 404

    alert_data = {
        'id': alert[0],
        'message': alert[1],
        'timestamp': alert[2]
    }

    return jsonify(alert_data)

if __name__ == '__main__':
    app.run(debug=True)


