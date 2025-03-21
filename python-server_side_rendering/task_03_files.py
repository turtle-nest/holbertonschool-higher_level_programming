from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)
"""
Flask application to display product data from JSON or CSV files using query parameters.
"""

def read_json_file():
    """
    Reads and returns the data from the products.json file.
    """
    with open('products.json') as file:
        return json.load(file)


def read_csv_file():
    """
    Reads and returns the data from the products.csv file.
    """
    products = []
    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products


@app.route('/products')
def products():
    """
    Displays product data based on the 'source' query parameter and filters by 'id' if provided.
    """
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Load data based on source
    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filter by product_id if provided
    if product_id:
        filtered_products = [product for product in products if int(product['id']) == product_id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products = filtered_products

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
