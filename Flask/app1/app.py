from flask import Flask, render_template, request
import numpy as np
import pickle
import sqlite3
import os
from flask import jsonify




app = Flask(__name__)
DB_FILE = 'predictions.db'


# Create DB and table if not exists
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kms_driven REAL,
                age REAL,
                power REAL,
                owner TEXT,
                brand TEXT,
                predicted_price REAL
            )
        ''')
init_db()

model = pickle.load(open('bike_model.pkl', 'rb'))
@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json
        kms_driven = float(data['kms_driven'])
        age = float(data['age'])
        power = float(data['power'])
        owner_text = data['owner']
        brand_text = data['brand']

        owner = owner_map[owner_text]
        brand = brand_map[brand_text]

        features = np.array([[kms_driven, age, power, owner, brand]])
        predicted_price = model.predict(features)[0]
        predicted_price = max(predicted_price, 0)

        # Save to DB
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute('''
                INSERT INTO predictions (kms_driven, age, power, owner, brand, predicted_price)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (kms_driven, age, power, owner_text, brand_text, predicted_price))

        return jsonify({'price': round(predicted_price, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/history')
def history():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM predictions ORDER BY id DESC").fetchall()
    return render_template('history.html', rows=rows)

from flask import send_file
import csv
import io

@app.route('/delete_all')
def delete_all():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("DELETE FROM predictions")
    return render_template('history.html', rows=[])

@app.route('/download_csv')
def download_csv():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM predictions ORDER BY id DESC")
        rows = cursor.fetchall()

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow([description[0] for description in cursor.description])  # headers
        writer.writerows(rows)

        output.seek(0)

        return send_file(
            io.BytesIO(output.getvalue().encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='prediction_history.csv'
        )



# Dictionaries to map user-friendly names to numeric values
brand_map = {
    'TVS': 0, 'Royal Enfield': 1, 'Triumph': 2, 'Yamaha': 3, 'Honda': 4,
    'Hero': 5, 'Bajaj': 6, 'Suzuki': 7, 'Benelli': 8, 'KTM': 9,
    'Mahindra': 10, 'Kawasaki': 11, 'Ducati': 12, 'Hyosung': 13,
    'Harley-Davidson': 14, 'Jawa': 15, 'BMW': 16, 'Indian': 17,
    'Rajdoot': 18, 'LML': 19, 'Yezdi': 20, 'MV': 21, 'Ideal': 22
}

owner_map = {
    'First Owner': 1,
    'Second Owner': 2,
    'Third Owner': 3,
    'Fourth Owner Or More': 4
}

@app.route('/')
def home():
    return render_template('home.html', brand_map=brand_map, owner_map=owner_map)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        kms_driven = float(request.form['kms_driven'])
        age = float(request.form['age'])
        power = float(request.form['power'])
        owner_text = request.form['owner']
        brand_text = request.form['brand']

        owner = owner_map[owner_text]
        brand = brand_map[brand_text]

        features = np.array([[kms_driven, age, power, owner, brand]])
        predicted_price = model.predict(features)[0]
        predicted_price = max(predicted_price, 0)  # 🚫 No negative predictions

        # Store in database
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute('''
                INSERT INTO predictions (kms_driven, age, power, owner, brand, predicted_price)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (kms_driven, age, power, owner_text, brand_text, predicted_price))

        # IMPORTANT CHANGE: Return JSON for the new UI, but can fall back to rendering a template
        # for other uses if needed.
        return jsonify({
            'prediction_text': f"₹{round(predicted_price, 2)}"
        })

    except Exception as e:
        # Return error as JSON too
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)
