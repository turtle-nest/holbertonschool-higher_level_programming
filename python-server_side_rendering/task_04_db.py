from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file():
    with open('products.json') as file:
        return json.load(file)

def read_csv_file():
    products = []
    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

def read_sqlite_db(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Access columns by name
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
            row = cursor.fetchone()
            return [dict(row)] if row else []
        else:
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    except sqlite3.Error as e:
        print("Database error:", e)
        return "Database error"
    finally:
        conn.close()

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        data = read_json_file()
    elif source == 'csv':
        data = read_csv_file()
    elif source == 'sql':
        data = read_sqlite_db(product_id)
        if data == "Database error":
            return render_template('product_display.html', error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtrage manuel pour JSON ou CSV
    if source in ['json', 'csv'] and product_id:
        filtered = [p for p in data if int(p['id']) == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        data = filtered

    if not data:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
